from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Note

# Create your views here.


def home_page(request):
    latest_note_list = Note.objects.order_by('-create_date')
    context = {
        "latest_note_list": latest_note_list,
    }
    return render(request, 'note/index.html', context)


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {
        "note": note
    }
    return render(request, 'note/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)