from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', views.register ,name='register'),
    path('profile/', views.profile ,name='profile'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('circle/',views.circle,name='circle'),
    path('feed/',views.feed,name='feed'),
    path('report/',views.report,name='report'),
    path('unfollow/<int:id>',views.unfollow,name='unfollow'),
    path('follow/<int:id>',views.follow,name='follow'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)