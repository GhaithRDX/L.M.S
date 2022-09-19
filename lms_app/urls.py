from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_user,name="login"),
    path('index/',views.index,name='index'),
    path('sign-up/', views.sign_up , name = 'sign_up'),
    path('books/',views.books,name='books'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

]