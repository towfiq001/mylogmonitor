from django.db import models

class LogHistory(models.Model):
    datetime = models.DateTimeField()
    category = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    
    class Meta:
        ordering = ['datetime', 'category']
    
    def __str__(self):
        """String for representing the Model object."""
        return '{0} {1} {2}'.format(self.datetime, self.category, self.message)


class LogByDate(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    
    class Meta:
        ordering = ['date', 'category']
    
    def __str__(self):
        """String for representing the Model object."""
        return '{0} {1} {2}'.format(self.date, self.category, self.message)