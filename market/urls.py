from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.book_list, name='book_list'),
#    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='market/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='market/logout.html'), name='logout'),
    path('home/', views.home, name='home'),
    path('search/', views.Search, name='search'),
    path('users/<int:pk>/', views.users_exhibit, name='users_exhibit'),
    path('photos/new/', views.photos_new, name='photos_new'),
    path('photos/<int:pk>/', views.photos_detail, name='photos_detail'),
    path('photos/<int:pk>/delete/', views.photos_delete, name='photos_delete'),
    path('photos/<str:lesson>/', views.photos_lesson, name='photos_lesson'),
    path('product/', views.product, name='product'),
    path('talk/', views.talk, name='talk'),
]
