from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Task(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name=_("title of task")
    )
    description = models.TextField(
        verbose_name=_("description of task")
    )
    completed = models.BooleanField(
        default=False,
        verbose_name=_("flag indicating whether the task is running")
    )
    created_at = models.DateTimeField(
        auto_created=True,
        auto_now_add=True,
        verbose_name=_("date and time the task was created")
    )

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
