from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .forms import *
from django.template.defaultfilters import slugify
class Home(ListView):
    model = Task # what a model will be use
    template_name ='todo_app/index.html'
    context_object_name = 'tasks' # name for my Task instance
    cats = Category.objects.all()
    extra_context = {'title':'Main Page','cats':cats}
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user) # what should be returned from db

class CategoryTask(ListView):
    model=Task
    template_name ='todo_app/index.html'
    context_object_name = 'tasks'
    cats = Category.objects.all()
    extra_context = {'title': 'Main Page', 'cats': cats}

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user,cat__slug=self.kwargs['cat_slug'])


class ReadMore(DetailView):
    model = Task
    template_name = 'todo_app/readmore.html'
    context_object_name = 'tasks'
    slug_url_kwarg = 'task_slug'
    cats = Category.objects.all()
    extra_context = {'title': 'Main Page', 'cats': cats}



def createtask(request):

    if request.method =='POST': #if we press buttom submit
        form = TaskForm(request.POST) # we generate форму которую заполнили для записи

        if form.is_valid():
            try:
                taskadd=form.save(commit=False)
                taskadd.author = request.user
                taskadd.slug = slugify(taskadd.title)
                taskadd.save()
                return redirect('home')
            except:
                    form.add_error(None,'Error')
    else:
        form = TaskForm() # если это первое открытие формы(то есть она будет пустой)
        cats = Category.objects.all()
        context = {"form": form, "cats": cats}
    return render(request,'todo_app/addtask.html',context) # рендерим  пустую страничку на основе модели формы

def edittask(request,pk):
    task = Task.objects.get(id = pk)
    form = EditForm(instance=task)
    context = {'form': form,'task':task}
    if request.method =='POST': # при нажатии кнопки
        form = EditForm(request.POST,instance=task)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Error')
    return render(request,'todo_app/edit.html',context) # при вызове по ссылке




class RegisterView(CreateView):
    template_name="todo_app/register.html"
    form_class = Register
    success_url =('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
   


class LoginUserView(LoginView):
    template_name = 'todo_app/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('home')


def DeleteTask(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('login')