from django.db import models

class TasksStore(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title