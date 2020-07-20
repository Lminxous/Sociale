from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='social-home'),
    path('user/<username>',views.user_post_view,name='user-posts'),
    path('post/new/', views.post_create_view, name = 'post-create'),
    path('post/<int:id>/update/', views.post_update_view, name = 'post-update'),
    path('post/<int:id>/', views.post_detail_view, name = 'post-detail'),
    path('post/<int:id>/delete/', views.post_delete_view, name = 'post-confirm-delete'),
    path('post/<int:id>/report/', views.post_report_view, name = 'post-report'),
    path('comment/<int:id>/update', views.comment_update_view, name = 'comment-update'),
    path('comment/<int:id>/delete', views.comment_delete_view, name = 'comment-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)