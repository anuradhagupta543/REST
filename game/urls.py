from django.conf.urls import include, url
from django.contrib import admin

# It is the first place where our web page lookes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^score/', include('score.urls')),
]
