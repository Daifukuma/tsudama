from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

market_name = 'market'
urlpatterns = [
    path('', views.book_list, name='book_list'),
#    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='market/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('users/<int:pk>/', views.users_exhibit, name='users_exhibit'),
    path('photos/new/', views.photos_new, name='photos_new'),
    path('photos/<int:pk>/', views.photos_detail, name='photos_detail'),
    path('photos/<int:pk>/delete/', views.photos_delete, name='photos_delete'),
    path('photos/<str:category>/', views.photos_category, name='photos_category'),
    path('product/', views.product, name='product'),
    path('talk/', views.talk, name='talk'),
]
