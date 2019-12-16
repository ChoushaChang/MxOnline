from django.shortcuts import render

from django.http import HttpResponse
import datetime
# Create your views here.
from apps.collector.models import Log

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def log(request):
    if request.method == 'POST':
        date = request.GET.get('date', datetime.datetime.now())
        user_id = request.POST['user_id']
        course_id = request.POST['course_id']
        event = request.POST['event_type']
        sess_id = request.POST['session_id']
        print(date)
        print(user_id)
        print(course_id)
        print(event)
        print(sess_id)
        print("request.method:",request.method)

        #check if user buy the course
        has_buy=Log.objects.filter(user_id=int(user_id),course_id=int(course_id),event='buy')
        fav_state=Log.objects.filter(user_id=int(user_id),course_id=int(course_id)).order_by("-created")[:5]
        if event=='moreDetail' or event=='OrgMoreDetail':
            save_to_log(date,user_id,course_id,event,sess_id)
        elif fav_state[0].event=="RemoveList" and event=='AddToList':
            save_to_log(date,user_id,course_id,event,sess_id)
        elif fav_state[0].event=="AddToList" and event=='RemoveList':
            save_to_log(date,user_id,course_id,event,sess_id)
        elif not has_buy and event=='buy':
            save_to_log(date,user_id,course_id,event,sess_id)

    else:
        HttpResponse('log only works with POST')
    return HttpResponse('ok')

def save_to_log(date,user_id,course_id,event,sess_id):
    l = Log(
        created=date,
        user_id=user_id,
        course_id=str(course_id),
        event=event,
        session_id=str(sess_id))
    l.save()