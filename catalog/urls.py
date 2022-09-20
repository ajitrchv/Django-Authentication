from django.urls import path
from . import views

app_name='catalog'

urlpatterns = [
    path('', views.index,name='index'),
    path('create_book/', views.BookCreate.as_view(), name='create_book'),
    path('addauthor/', views.AuthorCreate.as_view(), name='addauthor'),
    path('addlanguage/', views.LanguageCreate.as_view(), name='addlanguage'),
    path('addbookinstance/', views.BookInstanceCreate.as_view(), name='addbookinstance'),
    path('addgenre/', views.GenreCreate.as_view(), name='addgenre'),
    path('thanks/', views.ThanksView.as_view(), name="thanks"),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('my_view/',views.my_view, name='my_view'),
    path('signup/', views.SignUpView.as_view(),name= 'signup'),
    path('profile/', views.CheckoutBooks.as_view(),name= 'profile')
    
    
]
