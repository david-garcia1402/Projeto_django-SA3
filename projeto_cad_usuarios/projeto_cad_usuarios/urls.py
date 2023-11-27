from django.urls import path, include
from app_cad_usuarios import views

urlpatterns = [
    #rota. view responsável, nome de referencia
    
    #usuarios.com
    path('',views.home,name='home'),
    
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),

    #usuarios.com/editar
    path('editar/<int:id>', views.editar, name='editar'),

    path('update/<int:id>', views.update, name='update'),

    #usuarios.com/regras
    path('regras/',views.regras,name='regras'),

]