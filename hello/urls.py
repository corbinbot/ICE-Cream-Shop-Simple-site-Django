from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Vivek Shop Admin'
admin.site.site_title = 'Vivek Shop Admin'
admin.site.index_title = 'welcome to Vivek Shop'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myhome.urls'))
]
