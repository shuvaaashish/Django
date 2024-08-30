from django.shortcuts import render
tasks=["boo","baz","bald"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
