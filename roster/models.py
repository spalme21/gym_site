from django.db import models
from django.urls import reverse
from django.utils import timezone

class Client(models.Model):
    """Model representing a client."""
    last_name = models.CharField(max_length=32, help_text="Enter the last name")
    first_name = models.CharField(max_length=32, help_text="Enter the first name")
    email = models.EmailField(max_length=254, help_text="Enter the email")
    credits = models.IntegerField()

    def __str__(self):
        """String to represent the Client object"""
        return f"{self.last_name}, {self.first_name}"
    
    def get_absolute_url(self):
        """Returns the URL to access a specific client"""
        return reverse("client-detail-view", args=[str(self.id)])


class ClassType(models.Model):
    """Model representing a type of class."""
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    maximum_class_size = models.IntegerField()
    credit_cost = models.IntegerField()

    def __str__(self):
        """String to represent a class type"""
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a specific class type"""
        return reverse("classtype-detail-view", args=[str(self.id)])


class ClassSession(models.Model):
    """Model representing a specific session of a class."""
    class_type = models.ForeignKey(ClassType, on_delete=models.PROTECT)
    date_and_time = models.DateTimeField(default=timezone.now)
    roster = models.ManyToManyField(Client)

    class Meta:
        ordering = ["-date_and_time"]

    def __str__(self):
        """String to represent a specific session of a class."""
        return f"{self.class_type}: {self.date_and_time}"

    def get_absolut_url(self):
        """Returns the URL to access a specific session of a class."""
        return reverse("classsession-detail-view", args=[str(self.id)])
    