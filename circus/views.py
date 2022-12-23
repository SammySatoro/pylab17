from django.shortcuts import render, redirect
from .models import Arena, Artist, Show, Ticket, Visitor
from .forms import ArenaForm

class Context:

    def __init__(self, form, request):
        self.form = form
        self.request = request
        self.context = {
            'form': form
        }

    def post(self):
        error = ''
        if self.request.method == 'POST':
            form = self.form(self.request.POST)
            if form.is_valid():
                form.save()
            else:
                error = 'Invalid input format'
                self.context['error'] = error


def index(request):
    return render(request, 'circus/index.html')

def arena_delete_all(request):
    Arena.objects.all().delete()
    return redirect('arena')

def arena_delete(request, id):
    item = Arena.objects.get(id=id)
    item.delete()
    return redirect('arena')

def arena_update(request):
    id = 128

    item = Arena.objects.get(id=id)
    item.Name = request.POST.get('name', False)
    item.Location = request.POST.get('location', False)
    item.save()
    return redirect('arena')

def arena(request):
    context = Context(ArenaForm, request)
    context.post()
    data = Arena.objects.order_by('id')
    fields = ('ID', 'Name', 'Location')
    return render(request, 'circus/arena.html', {'title': 'Arena', 'data': data, 'context': context, 'fields': fields})


def show(request):
    data = Artist.objects.order_by('id')
    return render(request, 'circus/show.html', {'title': 'Show', 'data': data})


def ticket(request):
    data = Show.objects.order_by('id')
    return render(request, 'circus/ticket.html', {'title': 'Ticket', 'data': data})


def visitor(request):
    data = Ticket.objects.order_by('id')
    return render(request, 'circus/visitor.html', {'title': 'Visitor', 'data': data})


def artist(request):
    data = Visitor.objects.order_by('id')
    return render(request, 'circus/artist.html', {'title': 'Artist', 'data': data})
