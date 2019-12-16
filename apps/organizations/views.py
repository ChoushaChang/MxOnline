import uuid,random

from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q

from apps.organizations.models import CourseOrg
from apps.organizations.forms import AddAskForm
from apps.operations.models import UserFavorite

class OrgDescView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page":current_page,
            "has_fav":has_fav
        })


class OrgCourseView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        all_courses = course_org.course_set.all()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        # 对课程机构数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=16, request=request)
        courses = p.page(page)

        return render(request, "org-detail-course.html", {
            "all_courses": courses,
            "course_org": course_org,
            "current_page":current_page,
            "has_fav":has_fav
        })

class OrgHomeView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]

        return render(request, "org-detail-homepage.html", {
            "all_courses":all_courses,

            "course_org":course_org,
            "current_page": current_page,
            "has_fav":has_fav
        })


class AddAskView(View):
    """
    处理用户的咨询
    """
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status":"success"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg":"添加出錯"
            })


class OrgView(View):
    def get(self, request, *args, **kwargs):
        #从数据库中获取数据
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        keywords = request.GET.get("keywords", "")
        s_type = "org"
        if keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=keywords) | Q(desc__icontains=keywords))

        #通过机构类别对课程机构进行筛选
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        #对机构进行排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_orgs = all_orgs.order_by("-students")
        elif sort == "courses":
            all_orgs = all_orgs.order_by("-course_nums")

        org_nums = all_orgs.count()
        # 对课程机构数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=16, request=request)
        orgs = p.page(page)

        sess_id=session_id(request)
        u_id=user_id(request)
        return render(request, "org-list.html",{
            "all_orgs":orgs,
            "org_nums":org_nums,
            "category":category,
            "sort":sort,
            "hot_orgs":hot_orgs,
            "keywords": keywords,
            "s_type": s_type,
            "session_id":sess_id,
            "user_id":u_id,
        })

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
