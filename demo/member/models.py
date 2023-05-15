from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.TextField(defule="mmn_name")
    age = models.TextField(defule="777")
    last_modify_date = models.DateTimeField(auto_now = True)
    created = models.DurationField(auto_now_add = True)
    
    class Meta:
        db_table = "member"