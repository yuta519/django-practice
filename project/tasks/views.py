from django.views import generic

from tasks.models import Ticket, User


class UserIndexView(generic.ListView):
    model = User
    template_name = "tasks/user_list.html"


class UserDetailView(generic.DetailView):
    model = User
    template_name = "tasks/user_detail.html"


class TicketIndexView(generic.ListView):
    model = Ticket
    template_name ="tasks/ticket_list.html"


class TicketDetailView(generic.DetailView):
    model = Ticket
    template_name ="tasks/ticket_detail.html"
