from django.shortcuts import render

# Create your views here.
def inicioDef(request):
    return render(request, "inicio.html",{})
def musicaDef(request):
    return render(request, "musica.html",{})
def viajarDef(request):
    return render(request, "viajar.html",{})
def pensamientoDef(request):
    return render(request, "pensamiento.html",{})
def videoDef(request):
    return render(request, "video.html",{})