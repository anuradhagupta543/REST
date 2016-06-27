from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from score import views

# It is the first place where our web page lookes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scores/', views.ScoreList.as_view(), name='scores'),
    #  url(r'^scores/(?P<user_name>)/$', views.UpdateScore.as_view(), name='update'),
]
# It will enable extension support.
urlpatterns = format_suffix_patterns(urlpatterns)
