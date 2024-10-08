"""Define padrões de URL para learning_logs"""


from django.urls import path

from . import views


app_name = 'learning_logs'
urlpatterns = [
    #Pagina inicial
    path('', views.index, name='index'),
    #Pagina que mostra todos os tópicos
    path('topics/', views.topics, name='topics'),
    #Pagina de detalhes para um único topico
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]