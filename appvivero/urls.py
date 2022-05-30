from django.test import TestCase

# Create your tests here.
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from appvivero import views

urlpatterns = [
    path('', views.ViveroCreateView.as_view(), name='viverohome'),  #as_view() es porque estamos trabajando con vista basada en clases
    # path('registrovivero/', views.viveroview, name='registro_vivero'),
    path('registrovivero/', views.ViveroCreateView.as_view(), name='registro_vivero'),
    #Lista viveros
    path('listarviveros/', views.ViveroListarView.as_view(), name='listar_vivero'),
    path('editarviveros/<int:pk>/', views.ViveroEditar.as_view(), name='editar_vivero'),
    path('eliminarvivero/<int:pk>/', views.ViveroEliminar.as_view(), name='eliminar_vivero'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)