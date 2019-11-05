from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
#from .models import Photo
from .models import Textbook, Department
from django.contrib.auth.forms import UserCreationForm
from . import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from .forms import PhotoForm
from .forms import TextbookForm
from django.contrib import messages
from django.views.decorators.http import require_POST
#from .models import Photo, Category
from django.core.paginator import Paginator

def book_list(request):
    books = Textbook.objects.all()
    paginator = Paginator(all_articles, 5)
    p = request.GET.get('p')
    textbooks = paginator.get_page(p)
    return render(request, 'market/first.html', {'textbooks':textbooks})

def login(request):
    return render(request, 'market/login.html')

def home(request):
#    photos = Photo.objects.all().order_by('-created_at')
    textbooks = Textbook.objects.all().order_by('-created_at')
    return render(request, 'market/home.html', {'textbooks': textbooks})

def product(request):
    return render(request, 'market/product.html')

def talk(request):
    return render(request, 'market/talk.html')

def users_exhibit(request, pk):
    user = get_object_or_404(User, pk=pk)
#    photos = user.photo_set.all().order_by('-created_at')
    textbooks = user.textbook_set.all().order_by('-created_at')
    return render(request, 'market/users_exhibit.html', {'user': user, 'textbooks':textbooks})

def logout(request):
    return render(request, 'market/logout.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                login(request)
                return redirect('users_exhibit', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'market/signup.html', {'form': form})

@login_required  # ①
def photos_new(request):
    if request.method == "POST":
#        form = PhotoForm(request.POST, request.FILES)  # ②
        form = TextbookForm(request.POST, request.FILES)
        if form.is_valid():
            textbook = form.save(commit=False)  # ③
            textbook.user = request.user # ④
            textbook.save()  # ⑤
            messages.success(request, "投稿が完了しました！")
        return redirect('users_exhibit', pk=request.user.pk)
    else:
#        form = PhotoForm()
        form = TextbookForm()
    return render(request, 'market/photos_new.html', {'form': form})

def photos_detail(request, pk):
#    photo = get_object_or_404(Photo, pk=pk)
    textbook = get_object_or_404(Textbook, pk=pk)
    return render(request, 'market/photos_detail.html', {'textbook': textbook})

@require_POST
def photos_delete(request, pk):
#    photo = get_object_or_404(Photo, pk=pk)
    textbook = get_object_or_404(Textbook, pk=pk)
    textbook.delete()
    return redirect('users_exhibit', request.user.id)

def photos_department(request, department):
    # titleがURLの文字列と一致するCategoryインスタンスを取得
#    category = Category.objects.get(title=category)
#    lesson = Lesson.objects.get(title=lesson)
    department = Department.objects.get(title=department)
    # 取得したCategoryに属するPhoto一覧を取得
#    photos = Photo.objects.filter(category=category).order_by('-created_at')
#    textbooks = Textbook.objects.filter(lesson=lesson).order_by('-created_at')
    textbooks = Textbook.objects.filter(department=department).order_by('created_at')
    return render(request, 'market/home.html', {'textbooks': textbooks, 'department':department})
