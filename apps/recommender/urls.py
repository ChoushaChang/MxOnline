from django.conf.urls import url
from django.urls import path

from apps.recommender import views
from apps.recommender.views import RecsListView

urlpatterns = [
    url(r'^rec_list/$', RecsListView.as_view(), name="rec_list"),
    url(r'^association_rule/(?P<content_id>\w+)/$',
        views.get_association_rules_for,
        name='get_association_rules_for'),
    url(r'^ar/(?P<user_id>\w+)/$',
        views.recs_using_association_rules,
        name='recs_using_association_rules'),
]