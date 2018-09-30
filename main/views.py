from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Message
from .forms import MessageForm

def index(request):
    message = Message.objects.all()[0]
    return render(request, "main/index.html", {"message": message})

def onas(request):
    return render(request, "main/onas.html", {})

def fotky(request):
    return render(request, "main/fotky.html", {})

def planek(request):
    return render(request, "main/planek.html", {})

def odkazy(request):
    return render(request, "main/odkazy.html", {})

@login_required()
def login(request):
    return index(request)

@login_required()
def edit(request):
    message = get_object_or_404(Message, pk=1)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save()
            return redirect('index')
    else:
        form = MessageForm(instance=message)
    return render(request, "main/edit.html", {"form": form})
