from django.urls import path, include
from . import views

urlpatterns = [
    path('addRow/<int:idProduct>', views.addInCart, name='addInCart'),
    path('deleteRow/<int:idProduct>', views.deleteFromCart, name='addInCart'),
    path('', views.db_home, name='db_home')
    #127.0.0.1:8000/addInCart/addRow/
    #$("#new-nav").load("/test.html");
    #<ol id="new-nav"></ol>
]