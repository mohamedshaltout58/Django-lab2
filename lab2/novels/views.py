from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse ,JsonResponse
from novels.models import novels
# Create your views here.
def novelsHome(request):
    return HttpResponse("<h1>Welcome To Novels Home Page</h1>")

def readsHome(request, readname):
    return HttpResponse(f"<h1> Hi {readname}</h1>")

def returnlist(reques):
    names={"name":"mohamed", "Track":"DevOps"}
    return JsonResponse(names)

def getnovels(request):
    novelss = novels.objects.all()
    return render(request, "novels_index.html", context = {"novelss" : novelss})

def shownovels(request, id):
    #shownovels = novels.objects.get(id=id)
    shownovels = get_object_or_404(novels,id=id)
    return render(request,"shownovels.html", context = {"shownovels" : shownovels})

def deletenovels(request, id):
    delnovel = novels.objects.get(id=id)
    delnovel.delete()
    return redirect("novels")
