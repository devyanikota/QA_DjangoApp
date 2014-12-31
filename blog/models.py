from django.db import models
#from django.utils import timezone

#Creating models
class Question(models.Model):
    query = models.TextField()
    code = models.TextField()
    answer = models.CharField(max_length=200)
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    def dump(self):
        return (self.query, self.code, self.answer)

