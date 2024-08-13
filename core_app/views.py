from django.shortcuts import render
from .models import Topic


def index(request):
    return render(request, 'core_app/index.html')


def get_topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'core_app/topics.html', context)


def get_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries}

    return render(request, "core_app/topic.html", context)
