import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse, JsonResponse
from core.forms import NoteForm
from core.models import Note


@login_required
def index(request):
    context = {
        'notes': Note.objects.filter(user=request.user),
        'form': NoteForm()
    }
    return render(request, 'home.html', context)



@login_required
def add_note(request):
    # check if note is empty
    notes = Note.objects.filter(user=request.user)
    notesImpty = True 
    if notes:
        notesImpty = False 
    print(notesImpty)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
           
            if notesImpty:
                notes = Note.objects.filter(user=request.user)
                print(notes)
                print("hi ahmade")
                return render(request, 'home.html#notes-partial', {'notes': notes})
            else:
                return render(request, 'notes.html#todoitem-partial', {'note': note})
        else :
            return HttpResponse(
                status=500,
                headers={
                    'HX-Trigger': json.dumps({
                        'alert': 'somting wont wrong plees try again'
                    })
                })
    else :
        context = {'form': NoteForm(), 'impty': notesImpty}
        return render(request, 'form.html', context)
    


@login_required
def edit_note(request, pk):
    note = Note.objects.filter(user=request.user , pk=pk ).first()
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            context = {'note': note}
            return render(request, 'notes.html#todoitem-partial', context)
        else:
            return HttpResponse(
                status=500,
                headers={
                    'HX-Trigger': json.dumps({
                        'alert': 'somting wont wrong plees try again'
                    })
                })
    else :
        context = {'form' : NoteForm(instance=note), 'note':note}
        return render(request,"form.html" , context)
    

@login_required
@require_http_methods(['DELETE'])
def delete_note(request, pk):
    try:
        note = Note.objects.filter(user=request.user , pk=pk ).first()
        note.delete()
        notes = Note.objects.filter(user=request.user)
        if notes:
            response = HttpResponse(status=204)
            response['HX-Trigger'] = 'delete-note'
            return response
        else :
            print("hi ahmade")
            return render(request, 'home.html#notes-partial', {'notes': notes})
    except Exception as e:
        return HttpResponse(
                status=500,
                headers={
                    'HX-Trigger': json.dumps({
                        'alert': 'somting wont wrong plees try again'
                    })
                })
@login_required 
def search_view(request):
    query = request.GET.get('q', '') # Get the search query from the URL parameters
  
    notes = Note.objects.filter(user=request.user, tag__icontains=query)
    return render(request, 'home.html#notes-partial', {'query': query, 'notes': notes})


    