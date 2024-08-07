# it's advisable give your apps a default path too
# there can only be one default path per project and also per app


from django.urls import path

from . import views

app_name = "classes"
urlpatterns = [

    path('', views.Home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('add', views.add, name="add"),
    path('viewdata', views.viewdata, name="viewdata"),
    path('delete/<id>', views.delete, name="delete"),
    path('insertdata', views.insertdata, name="insertdata"),
    path('edit/<id>', views.edit, name="edit"),
    path('details/<id>', views.details, name="details")
]
