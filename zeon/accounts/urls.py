from django.conf.urls import url
from . import views

urlpatterns = [
    url("register", views.register, name='register'),
    url("login", views.login, name='login'),
    url("logout", views.logout, name='logout'),
<<<<<<< HEAD

=======
>>>>>>> 55aa9b47143832b2386e20a8c60c64f8ae032bea
]