from django.conf.urls import url
from django.contrib import admin
# It is the first place where our web page lookes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
