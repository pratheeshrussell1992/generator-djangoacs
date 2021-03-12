from django.db import models


# https://www.geeksforgeeks.org/creating-custom-user-model-using-abstractuser-in-django_restframework/

# https://hashedin.com/blog/configure-role-based-access-control-in-django/
class Sample(models.Model): 
  firstname = models.CharField(max_length = 100, blank = False, null = True) 
  lastname = models.CharField(max_length = 100, blank = False, null = True)
  class Meta:
      permissions = (
       ("access_sample", "can access sample api"),)
