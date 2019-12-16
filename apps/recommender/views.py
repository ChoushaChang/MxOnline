import uuid,random
from django.shortcuts import render

from django.http import JsonResponse
from django.db.models import Avg, Count

from apps.collector.models import Log
from apps.recommender.models import SeededRecs

from django.views.generic.base import View
from apps.courses.models import Course

class RecsListView(View):
    def get(self, request, *args, **kwargs):
        sess_id=session_id(request)
        u_id=user_id(request)
        return render(request, "recommender_for_me.html",{
            "session_id":sess_id,
            "user_id":u_id,
        })

def get_association_rules_for(request, content_id, take=6):

    data = SeededRecs.objects.filter(source=content_id) \
               .order_by('-confidence') \
               .values('target', 'confidence', 'support')[:take]
    for i in range(len(data)):
        Course_list=list(Course.objects.filter(id=data[i]['target']).values())
        #print(Course_list)
        data[i]['Course_obj']=Course_list

    #Course_data = Course.objects.filter(course_id=data)
    #print(data)
    return JsonResponse(dict(data=list(data)), safe=False)


def recs_using_association_rules(request, user_id, take=6):
    events = Log.objects.filter(user_id=user_id)\
                        .order_by('created')\
                        .values_list('Course_or_Org_id', flat=True)\
                        .distinct()

    seeds = set(events[:20])

    rules = SeededRecs.objects.filter(source__in=seeds) \
        .exclude(target__in=seeds) \
        .values('target') \
        .annotate(confidence=Avg('confidence')) \
        .order_by('-confidence')

    recs = [{'id': '{0:07d}'.format(int(rule['target'])),
             'confidence': rule['confidence']} for rule in rules]

   # print("recs from association rules: \n{}".format(recs[:take]))
    return JsonResponse(dict(data=list(recs[:take])))

def session_id(request):
    #print("session_id function2",request.session.session_key)
    if request.session.session_key:
        request.session["session_id"]=request.session.session_key
    elif not "session_id" in request.session:
        request.session["session_id"] = str(uuid.uuid1())
    return request.session["session_id"]

def user_id(request):
    user_id = request.user.id

    if user_id:
        request.session['user_id'] = user_id

    if not "user_id" in request.session:
        request.session['user_id'] = random.randint(10000000000, 90000000000)

    #print("ensured id: ", request.session['user_id'] )
    return request.session['user_id']