from django.urls import path

from . import views

app_name = 'core_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.get_topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.get_topic, name='topic')
]
