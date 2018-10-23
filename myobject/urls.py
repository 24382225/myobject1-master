from django.conf.urls import url,include
#from django.contrib import admin

urlpatterns = [
#   url(r'^admin/', admin.site.urls),
    url(r'^myadmin/', include('myadmin.urls')), #网站后台路由
    url(r'^', include('web.urls')),           #网站前台路由
]