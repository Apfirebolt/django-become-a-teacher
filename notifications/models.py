from django.db import models


# Create your models here.
class PHDNotification(models.Model):
    program_name = models.CharField("Program Name", max_length=200)
    college_name = models.CharField("College Name", max_length=200)
    stipend_available = models.BooleanField("Stipend Availability", default=True)
    vacancies = models.IntegerField("Vacancies", default=0)
    stipend_amount = models.FloatField("Stipend Amount")
    program_fees = models.FloatField("Program Fees")
    gate_required = models.BooleanField("Gate Exam Required", default=True)
    ugc_net_required = models.BooleanField("UGCNET Exam Required", default=False)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    website_url = models.URLField("Program URL")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)


    def __str__(self):
        return str(self.program_name) + '-' + str(self.college_name)

    class Meta:
        verbose_name_plural = "PHD Notifications"


class FacultyNotification(models.Model):
    post_name = models.CharField("Post Name", max_length=200)
    college_name = models.CharField("College Name", max_length=200)
    vacancies = models.IntegerField("Vacancies", default=0)
    salary_per_month = models.FloatField("Per Month Salary")
    phd_required = models.BooleanField("PHD Required", default=True)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    website_url = models.URLField("Post URL")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    def __str__(self):
        return str(self.post_name) + '-' + str(self.college_name)

    class Meta:
        verbose_name_plural = "Faculty Notifications"
