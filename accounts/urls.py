from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:account_pk>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('<int:account_pk>/follow/', views.follow, name='follow'),
]