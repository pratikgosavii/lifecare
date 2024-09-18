from django.db import models


from datetime import datetime, timezone






class customer(models.Model):
    
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class test_type(models.Model):
    
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class record(models.Model):
    
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    test_type = models.ForeignKey(test_type, on_delete=models.CASCADE)
    dr = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)


    def __str__(self):
        return self.customer.name


class payment(models.Model):
    
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now=False)
    remark = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.customer.name