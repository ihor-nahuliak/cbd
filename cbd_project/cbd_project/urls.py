from django.urls import include, path
from django.contrib import admin
admin.autodiscover()
from cbd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save_coding/', views.save_coding, name='save_coding'),
    path('moderate/', views.moderate, name='moderate'),
    path('logout/',  views.user_logout, name='logout'),
]
