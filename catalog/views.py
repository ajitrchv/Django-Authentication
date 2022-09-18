from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView, DetailView
# Create your views here.
from .models import Book, Author, BookInstance, Genre, Language

def cathome(request):
    return HttpResponse('<h1>Welcome to Catalog Home</h1>')

def index(request):
    num_book = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    context = {
        'num_books':num_book,
        'num_intances':num_instances,
        'num_instances_available':num_instances_available,
    }
    
    return render(request,'catalog/index.html',context=context)

class BookCreate(CreateView):
    model = Book
    fields ='__all__'
    success_url= 'catalog:book_detail'

class BookDetail(DetailView):
    model = Book
    
   

class ThanksView(TemplateView):
    template_name= 'classroom/thanks.html'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url: 'catalog/thanks.html'

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'
    success_url: 'catalog/thanks.html'
    
class LanguageCreate(CreateView):
    model = Language
    fields = '__all__'
    success_url: 'catalog/thanks.html'
    
    def get_absolute_url(self):
        return f'catalog/thanks.html'
   
    
class BookInstanceCreate(CreateView):
    model = BookInstance
    fields = '__all__'
    success_url: 'catalog/thanks.html'
    
    
    


    
