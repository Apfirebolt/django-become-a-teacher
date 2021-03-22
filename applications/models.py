from django.db import models
from phd_teacher.settings import AUTH_USER_MODEL
from notifications.models import FacultyNotification, PHDNotification


# Create your models here.
class Application(models.Model):
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_phd_application = models.ForeignKey(PHDNotification, on_delete=models.CASCADE, blank=True, null=True)
    is_faculty_application = models.ForeignKey(FacultyNotification, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.CharField("Application Notes", max_length=200)
    has_applied = models.BooleanField("Applied", default=False)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)


    def __str__(self):
        return str(self.program_name) + '-' + str(self.college_name)

    class Meta:
        verbose_name_plural = "Applications"


