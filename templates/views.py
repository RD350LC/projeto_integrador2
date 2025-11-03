from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def obras(request):
    return render(request, 'obras.html')

def projetos(request):
    return render(request, 'projetos.html')

def contato(request):
    return render(request, 'contato.html')