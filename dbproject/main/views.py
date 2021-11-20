from django.shortcuts import render
from .models import *
# Create your views here.
# Model >> objects - manager
# objects.all() >> hamma elem
# objects.get(id=12) >>params >> faqat bitta elem
# objects.first()
# objects.last()
# objects.filter() >> params
# objetcs.create()
# objects.delete()
# objects.save()

# objects.get_or_create(name="Damas")
# objects.update_or_create(name="Damas")


def homeView(request):
    if request.method == 'POST':
        value = request.POST.get("myValue")
        createNewMachine = Machine.objects.create(name=value)
        createNewMachine.save()
    context = {
        "students":Student.objects.first(),
        "rooms":Room.objects.last(),
        "teachers":Teacher.objects.all(),
        "machines":Machine.objects.all()
    }
    return render(request, "index.html", context)