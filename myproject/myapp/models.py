from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)   # ✅ THIS LINE IMPORTANT
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    qualification = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    salary = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.job.title}"
# Create your models here.
