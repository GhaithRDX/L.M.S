from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import BookForm,CategoryForm,RegisterForm
from django.contrib.auth import login , logout, authenticate 
from django.contrib.auth.decorators import login_required,permission_required
from django.template import RequestContext
from django.contrib import messages
from django.views import View     
from django.contrib.auth.models import Group


@login_required(login_url="/login")
@permission_required('lms_app.add_book',login_url='/login',raise_exception=True)
@permission_required('lms_app.view_book',login_url='/login',raise_exception=True)
@permission_required('lms_app.add_category',login_url='/login',raise_exception=True)

def index(request):
    
    if request.method == 'POST':        
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    
    solds = Book.objects.filter(status='sold')
    all_solds = 0
    for x in solds :
        if x.price != None:
            all_solds += x.price
            
    rentals = Book.objects.filter(status='rental')
    
    all_rentals = 0
    for x in rentals :
        if x.total_rental != None:
            all_rentals += x.total_rental
        
    all_incomes = all_rentals + all_solds
        
    content = {
        'books':Book.objects.all(),
        'categs':Category.objects.all(),
        'form':BookForm(),
        'formC':CategoryForm(),
        'numbooks':Book.objects.filter(active=True).count(),
        'soldbooks':Book.objects.filter(status='sold').count(),
        'rentalbooks':Book.objects.filter(status='rental').count(),
        'availablebooks':Book.objects.filter(status='available').count(),
        'rentals':all_rentals,
        'solds':all_solds,
        'incomes':all_incomes,
        
    }
    return render(request,'pages/index.html',content)

@login_required(login_url='/login')
@permission_required('lms_app.view_book',login_url='/login',raise_exception=True)
def books(request):
    
    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
        
    
    search = Book.objects.all()
    title =None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    
    
    content = {
        'categs':Category.objects.all(),
        'formC':CategoryForm(),
        'books':search,

    }
    return render(request,'pages/books.html',content)

@login_required(login_url='/login')
@permission_required('lms_app.update_book',login_url='/login',raise_exception=True)
def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST,request.FILES,instance = book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance = book_id)
    content = {
        'form':book_save,
    }
    return render(request,'pages/update.html',content)


@login_required(login_url='/login')
@permission_required('lms_app.delete_book',login_url='/login',raise_exception=True)
def delete(request,id):
    book_id = get_object_or_404(Book,id=id)
    if request.method =='POST':
        book_id.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
    

def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/')
        else :
            messages.error(request, 'invalid username or password.')
    return render(request,'registration\login.html')    
            
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            my_group = Group.objects.get(name='group1') 
            my_group.user_set.add(user)      
            login(request,user)
            return redirect('/')

        
    else :
        form = RegisterForm()
    return render(request,'registration\sign_up.html',{"form":form})
    
    
        
            
        
    """
        form_class = RegisterForm
        initial = {'key': 'value'}
        template_name = 'registration/sign_up.html'
        
        def get(self, request, *args, **kwargs):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        
        def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)

            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')

                return redirect(to='/')

            return render(request, self.template_name, {'form': form})
        """
        