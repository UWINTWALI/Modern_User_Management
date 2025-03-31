from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<int:pk>/', views.user_update, name='user_update'),
    path('delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('details/<int:user_id>/', views.user_detail, name='user_detail'),
    path('search_location/', views.search_location, name='search_location'), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








