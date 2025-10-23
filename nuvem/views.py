from django.shortcuts import render

def nuvem_home(request):
    return render(request, 'nuvem_home.html')

def acompanhamento_obra(request):
    andamento = [
        {"etapa": "Fundações", "status": "Concluída", "data": "2025-07-10"},
        {"etapa": "Estrutura", "status": "Em andamento", "data": "2025-09-08"},
        {"etapa": "Acabamento", "status": "Pendente", "data": "-"},
    ]
    return render(request, 'acompanhamento_obra.html', {"andamento": andamento})