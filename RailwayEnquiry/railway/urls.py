from django.urls import path
from . import views


urlpatterns = [
    path("", views.login1, name="login"),
    path("logout/", views.logout1, name="logout"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
    path("ticketlist/", views.ticket_list, name="ticketlist"),
    path("trainlist/", views.train_list, name="trainlist"),
    path("addtrain/", views.add_train, name="addtrain"),
    path("addticket/", views.add_ticket, name="addticket"),
    path("addpassenger/", views.add_passenger, name="addpassenger"),
    path("deleteticket/<int:id>", views.delete_ticket, name="deleteticket"),
]
