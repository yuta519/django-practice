from django.urls import reverse
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

    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


class TicketUpdateView(generic.UpdateView):
    model = Ticket
    template_name ="tasks/ticket_update.html"
    fields = ['title', 'status', 'assigned_to']
    # success_url = '/tasks/tickets'

    def get_success_url(self) -> str:
        return reverse('tasks:tickets')

class TicketAssignView(generic.UpdateView):
    model = Ticket
    template_name ="tasks/ticket_assign.html"
    fields = ['assigned_to']

    def get_success_url(self) -> str:
        return reverse('tasks:tickets')
