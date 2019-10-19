import xadmin

from apps.organizations.models import CourseOrg

class CourseOrgAdmin(object):
    list_display = ['name', 'click_nums', 'fav_nums']
    search_fields = ['name', 'click_nums', 'fav_nums']
    list_filter = ['name', 'click_nums', 'fav_nums']
    style_fields = {
        "desc": "ueditor"
    }
    readonly_fields=['click_nums','fav_nums','students','course_nums']

xadmin.site.register(CourseOrg, CourseOrgAdmin)