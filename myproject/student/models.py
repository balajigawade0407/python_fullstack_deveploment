from django.db import models

class Student_table(models.Model):
    reg_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(default='example@gmail.com')
    marks = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name or str(self.reg_no)