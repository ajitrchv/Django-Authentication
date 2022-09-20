from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Book, Author, BookInstance, Genre, Language

def cathome(request):
    return HttpResponse('<h1>Welcome to Catalog Home</h1>')

def index(request):
    num_book = Book.objects.all().count()
    book_data=Book.objects.all()
    num_instances = BookInstance.objects.all().count()
    authors = Author.objects.all()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    context = {
        'num_books':num_book,
        'num_intances':num_instances,
        'num_instances_available':num_instances_available,
        'book_data':book_data,
        'authors':authors,
    }
    
    return render(request,'catalog/index.html',context=context)



class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields ='__all__'
    success_url= "/catalog/thanks/"
  


class BookDetail(DetailView):
    model = Book
    
   

class ThanksView(TemplateView):
    template_name= 'catalog/thanks.html'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url= "/catalog/thanks/"

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'
    success_url= "/catalog/thanks/"
class LanguageCreate(CreateView):
    model = Language
    fields = '__all__'
    success_url= "/catalog/thanks/"
    
    def get_absolute_url(self):
        return f'catalog/thanks.html'
   
    
class BookInstanceCreate(CreateView):
    model = BookInstance
    fields = '__all__'
    success_url= "/catalog/thanks/"
    
@login_required   
def my_view(request):
    return render(request, 'catalog/my_view.html')



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'
