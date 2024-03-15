from members.models import Event, Message
from members.forms import EventForm
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from django.db.models import Q
import itertools
import locale
from datetime import datetime, timedelta
from collections import defaultdict
import json


def permission_check_2(user):
    try:
        return user.profile.permission_level > 2
    except AttributeError:  # anonymous user
        return False


def get_section(request):
    locale.setlocale(locale.LC_TIME, "de_DE")
    ddate = datetime.today() + timedelta(days=7)  # show older events for 1 more week

    # query for events that happen in the next year
    q = Event.objects.filter(Q(start_date__gte=ddate) & Q(deleted=False))

    nested_dict = lambda: defaultdict(nested_dict)
    events = nested_dict()

    for key, entries in itertools.groupby(q, lambda x: x.start_date.strftime("%B-%Y")):
        month, year = key.split("-")
        # add the entries for a year and a month to the dict
        events[year][month] = list(entries)

    messages = Message.objects.filter(display="events").distinct()

    context = {
        "events": events,
        "messages": messages,
    }

    return render(request, "sections/event_section.html", context)


#
#
# For the detail-view
#
#


def event_test_func(request, event):
    # members can see all events, otherwise if public event
    return any([request.user.is_authenticated, event.public_event])


class EventDetailView(UserPassesTestMixin, DetailView):
    template_name = "pages/event_detail.html"
    model = Event

    def test_func(self):
        event = self.get_object()
        return event_test_func(self.request, event)


#
#
# The Event Form
#
#


@user_passes_test(permission_check_2)
def toggle_delete(request):
    object = Event.objects.get(pk=int(request.GET.get("id")))
    object.deleted = object.deleted == False  # toggle the deletion
    object.save()
    return render(request, "snippets/events/event_header.html", {"event": object})


class EventCreateView(UserPassesTestMixin, CreateView):
    # template: event_detail.html
    model = Event
    form_class = EventForm
    template_name = "pages/event_form.html"

    def test_func(self):
        try:
            return self.request.user.profile.permission_level > 2
        except AttributeError:
            return False


class EventUpdateView(UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "pages/event_form.html"

    def test_func(self):
        try:
            return self.request.user.profile.permission_level > 2
        except AttributeError:
            return False


@user_passes_test(permission_check_2)
def add_question(request):
    object = Event.objects.get(pk=int(request.POST.get("id")))
    questions = (
        json.loads(object.questions) if object.questions else {}
    )  # get the (empty) questions json
    newkey = (
        max([int(x) for x in questions.keys()]) + 1 if len(questions.keys()) > 0 else 1
    )  # define a new key

    questions[newkey] = (
        request.POST.get("question"),
        request.POST.get("question_type"),
    )
    object.questions = json.dumps(questions)
    object.save()

    return render(
        request,
        "snippets/events/event_questions.html",
        {"event": object},
    )


@user_passes_test(permission_check_2)
def remove_question(request):
    object = Event.objects.get(pk=int(request.POST.get("id")))
    questions = json.loads(object.questions)

    del questions[request.POST.get("removekey")]

    object.questions = json.dumps(questions)
    object.save()

    return render(
        request,
        "snippets/events/event_questions.html",
        {"event": object},
    )


urlpatterns = [
    path("get-section", get_section, name="get_event_section"),
    path("<int:pk>", EventDetailView.as_view(), name="get_event_detail"),
    path("delete_toggle", toggle_delete, name="event_delete_toggle"),
    path("neu/", EventCreateView.as_view(), name="event_create"),
    path("<int:pk>/update", EventUpdateView.as_view(), name="event_update"),
    path("add-question", add_question, name="event_add_question"),
    path("remove-question", remove_question, name="event_remove_question"),
]
