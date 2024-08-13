from django.urls import path

from . import views

app_name = 'core_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.get_topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.get_topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.add_new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.add_new_entry, name='new_entry'),
    # Page for editing an entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),


]
