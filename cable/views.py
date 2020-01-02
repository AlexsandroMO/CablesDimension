
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ResidencDimens
from .forms import ResidencDimensForm
import main
from django import db


def home(request):

    #db.reset_queries()
    return render(request, 'cable/home.html')

def taskList(request):

    tasks = ResidencDimens.objects.all().order_by('-local')

    return render(request, 'cable/lista-circuitos.html',{'tasks': tasks})

def newTask(request):


    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            task.corrente_a = (task.total_va / task.tensa_va)

            queda = task.sessao_condutor
            test = main.read_sql_queda(queda)
            queda_tensao = test['queda_tesao'][0]
            
            print(test['queda_tesao'][0])
            print(task.total_va)
            print(task.corrente_a)
            print(task.tensa_va)
            print(task.quant)
            print(task.potencia_va)
            print(task.comprimento)
            #print((queda_tensao * task.corrente_a))

            #calc = ((((queda_tensao * task.corrente_a) * task.comprimento) / 1000) / task.total_va)
            #print('\n\nCalc: ', calc, '\n\n')

            task.queda_tensao_ckt = 0
            #task.queda_tensao_ckt = ((((test['queda_tesao'][0] * task.corrente_a) * task.comprimento) / 1000) / task.total_va)
            
            task.save()

            return redirect('/')

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form})


def helloworld(request):
    return HttpResponse('Hello World!')


