from django.db import models


class User(models.Model):
    user_name = models.CharField("name", max_length=15)
    user_email = models.EmailField("email")
    is_adult = models.BooleanField("adult")

    def __str__(self):
        return self.user_name


class Feedback(models.Model):
    feedback = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_date = models.DateTimeField("date", null=True, blank=True)
    opinion = models.TextField("feedback", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.feedback

