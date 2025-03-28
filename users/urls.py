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
    
    # dependent inputs for location selections
    
    path('get_provinces/<int:country_id>/', views.get_provinces, name='get_provinces'),
    path('get_districts/<int:province_id>/', views.get_districts, name='get_districts'),
    path('get_sectors/<int:district_id>/', views.get_sectors, name='get_sectors'),
    path('get_cells/<int:sector_id>/', views.get_cells, name='get_cells'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








