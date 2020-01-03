
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ResidencDimens
from .forms import ResidencDimensForm
from django.contrib import messages
import main
from django import db


def home(request):

    #db.reset_queries()
    return render(request, 'cable/home.html')

def taskList(request):

    task = ResidencDimens.objects.all().order_by('-local')

    return render(request, 'cable/lista-circuitos.html',{'task': task})

def newTask(request):


    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------
 
            t_va = float(task.total_va)

            task.corrente_a = (float(task.total_va) / t_va)
            #--------------------------------------------------
            queda = task.sessao_condutor
            test = main.read_sql_queda(queda)
            queda_tensao = test['queda_tesao'][0]

            calc = ((((float(queda_tensao) * float(task.corrente_a)) * float(task.comprimento)) / (1000) / t_va))

            task.queda_tensao_ckt = calc * 100
            
            if (float(task.queda_tensao_perm) / 100)< task.queda_tensao_ckt:
                task.queda_tensao_test = 'OK'
            else:
                task.queda_tensao_test = 'NÃO'
            #--------------------------------------------------
            corr = task.sessao_condutor
            test = main.read_sql_corr(corr)
            corrente = test['capacidade_conducao'][0]

            if corrente > float(task.corrente_a):
                task.capacidade_corrente = 'OK'
            else:
                task.capacidade_corrente = 'NÀO'
            #--------------------------------------------------
            dj = task.corrente_nominal
            test = main.read_sql_dj(dj)
            djj = int(test['dj'][0])

            if djj > (float(task.corrente_a) * 1.1):
                task.verifica_dj = 'OK'
            else:
                task.verifica_dj = 'NÀO'
            #--------------------------------------------------

            task.save()

            return redirect('task-list')

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form})


def editTask(request, id):

    task = get_object_or_404(ResidencDimens, pk=id)
    form = ResidencDimensForm(instance=task)

    if request.method == 'POST':
        form = ResidencDimensForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('task-list')
        else:
            return render(request, 'cable/edit-task.html', {'form': form, 'task': task})

    else:
        return render(request, 'cable/edit-task.html', {'form': form, 'task': task})


def deleteTask(request, id):
    task = get_object_or_404(ResidencDimens, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('task-list')

def helloworld(request):
    return HttpResponse('Hello World!')


