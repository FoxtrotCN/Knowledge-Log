from django.shortcuts import render, redirect

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


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


def add_new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_app:topics')

    context = {'form': form}
    return render(request, "core_app/new_topic.html", context)


def add_new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('core_app:topic', topic_id=topic_id)

    context = {'topic': topic,
               'form': form}
    return render(request, 'core_app/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_app:topic', topic_id=topic.id)

    context = {'entry': entry,
               'topic': topic,
               'form': form}
    return render(request, 'core_app/edit_entry.html', context)
