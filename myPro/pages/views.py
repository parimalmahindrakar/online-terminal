from django.shortcuts import render
from .models import Command
from .forms import commandForm
import subprocess,os

# Create your views here.


def cmd(request, *args, **kwargs):
    form = commandForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = commandForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def output(request, *args, **kwargs):
    commandSet = Command.objects.all()
    for i in commandSet:
        command_ = i.command
    data = subprocess.run(f'{command_} > cat.txt',
                          capture_output=True, shell=True)
    f = open('cat.txt')
    context = {
        'data': f
    }
    commandSet.delete()
    os.system("rm -rf cat.txt")
    return render(request, "index.html", context)
