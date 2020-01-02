
from django.test import TestCase

# Create your tests here.


#https://www.geeksforgeeks.org/textfield-django-models/


#pip3 install django-crispy-forms

#Zerar senha do admin
#python manage.py shell
#from django.contrib.auth.models import User
#User.objects.filter(is_superuser=True)

#usr = User.objects.get(username='nome-do-administrador')
#usr.set_password('nova-senha')
#usr.save()



'''Upload documents on Github
git clone <nome>
<entra na pasta criada>
git add .
git commit -m "texto"
git push
'''

'''git checkout -b nome cria uma branch
git checkout nome entra na branch
git branch - verifica as branchs
git checkout master - entra na master
git merge origin "nome" 
git push origin master - subir commit
git branch -D "nome"- deletar branch
'''


#Heroku
#https://github.com/Gpzim98/django-heroku

#git add .gitignore
#colocar no gitignore
'''.idea
.pyc
.DS_Store
*.sqlite3'''

'''
Publishing the app
git add .
git commit -m "Configuring the app"
git push heroku master --force
'''




'''

def newTask(request):


    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            task.corrente_a = (task.total_va / task.tensa_va)

            #queda = task.sessao_condutor
            #test = main.read_sql_queda(queda)

            #task.queda_tensao_ckt = ((((test['queda_tesao'] * task.corrente_a) * task.comprimento) / 1000) / task.total_va)

            task.save()

            return redirect('/')

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form})


'''
