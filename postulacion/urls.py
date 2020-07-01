from django.urls import path
from . import views

urlpatterns = [
    path('', views.postulacion, name='postulacion'),
    path('delete_postulante/<int:my_id>', views.delete_postulante, name='delete_postulante')
]
