from django.views import generic

from tasks.models import User

class UserIndexView(generic.ListView):
    model = User
    template_name = "templates/user_list.html"
