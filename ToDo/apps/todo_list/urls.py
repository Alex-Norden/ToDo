from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('delete/<list_id>', views.delete, name='delete'),
	path('is_done/<list_id>', views.is_done, name='is_done'),
	path('is_not_done/<list_id>', views.is_not_done, name='is_not_done'),
	path('edit/<list_id>', views.edit, name='edit'),
]