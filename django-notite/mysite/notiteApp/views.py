from django.shortcuts import render, redirect
import datetime
from .models import Note


def index(request):
    # toate notitele pe care le am le iau din baza de date si le pun intr-un dictionar numit 'context'
    context = {}
    notes = Note.objects.all() 
    context['notes'] = notes
    return render(request, "notiteApp/home.html", context)


#metoda pentru adaugarea notitelor.
def add(request):
    context = {}

    if request.method == "POST":
        title = request.POST['note-title']
        content = request.POST['note-content']
        importance = request.POST['note-importance']

        note = Note(title=title, content=content, importance=importance)
        note.save()
        return redirect('notiteApp:index')

    return render(request, "notiteApp/add.html", context)


#metoda pentru stergerea notitelor
def delete(request, id):
    context = {}

    if request.method == "POST":
        note = Note.objects.get(id=id)
        note.delete()
        return redirect('notiteApp:index')

    return redirect('notiteApp:index')