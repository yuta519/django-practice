from django.db import models
from django.forms import ValidationError


class Status(models.IntegerChoices):
    TODO = 1, 'ToDo'
    ONGOING = 2, 'Ongoing'
    PENDING = 3, "Pending"
    REVIEW = 4, "Review"
    DONE = 5, "Done"

    def __str__(self):
        return [i.value for i in Status]


class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    status = models.IntegerField(choices=Status.choices, default=Status.TODO)
    assigned_to = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE, null=True, default=None
    )
    created_at = models.DateField("Created Time",  auto_now_add=True)
    updated_at = models.DateField("Updated Time",  auto_now=True)

    def clean(self):
       if self.status != Status.TODO and not self.assigned_to:
        raise ValidationError("You must set assigner unless status is ToDo.")

    def __str__(self):
        return f'{self.title} by {self.assigned_to.name}'