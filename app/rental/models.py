from django.db import models
import random,uuid

from twilio.rest import Client

# Create your models here.
class Tenant(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50,null=True,blank=True)

    account_sid = 'ACa919fcc9e19f6a845d0b4ba32f9a58a7'
    auth_token = 'a9bb1a8cda45fca2b958c04b6cb5a3f5'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body= 'Join Earths mightiest heroes Like Kevin Bacon.',
                     from_='+16203250372',
                     to='+256705082827'
                 )

    print(message.sid)

    class Meta:
        verbose_name = ("Tenant")
        verbose_name_plural = ("Tenant")

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse("Tenant_detail", kwargs={"pk": self.pk})

   



    

class Property(models.Model):
    building_type= models.CharField(max_length=50)
    number_of_rooms=models.IntegerField()
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Property")
        verbose_name_plural = ("Property")

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse("Property_detail", kwargs={"pk": self.pk})

class Room(models.Model):
    STATUS1_TYPE_CHOICES=[
        ('Single','Single'),
        ('Double','Double')
    ]
    room_type=models.CharField(choices=STATUS1_TYPE_CHOICES,default='Single',max_length=50)
    property = models.ForeignKey(Property,on_delete=models.CASCADE,
    null=True,blank=True,related_name='property_name')

    class Meta:
        verbose_name = ("Room")
        verbose_name_plural = ("Room")

    def __str__(self):
        return f'{self.room_type} - {self.property}'

    def get_absolute_url(self):
        return reverse("Room_detail", kwargs={"pk": self.pk})

class Contract(models.Model):
    tenant= models.ForeignKey(Tenant,on_delete=models.CASCADE,
    null=True,blank=True,related_name='tenant_names')
    room = models.ForeignKey(Room,on_delete=models.CASCADE,
    null=True,blank=True,related_name='room_name')
    monthly_rent_due=models.CharField(max_length=50)
    date_begin= models.DateField()
    date_end= models.DateField()

    class Meta:
        verbose_name = ("Contract")
        verbose_name_plural = ("Contract")

    def __str__(self):
        return f'{self.room} - {self.tenant}-{self.monthly_rent_due}'

    def get_absolute_url(self):
        return reverse("Contract_detail", kwargs={"pk": self.pk})

class Payment(models.Model):
    def random_string():
        return str(random.randint(10000, 99999))
    
    tenant= models.ForeignKey(Tenant,on_delete=models.CASCADE,
    null=True,blank=True,related_name='tenant_name')
    contract= models.ForeignKey(Contract,on_delete=models.CASCADE,
    null=True,blank=True,related_name='contract_name')
    date_paid = models.DateField()
    monthly_rent_due= models.ForeignKey(Contract,on_delete=models.CASCADE,
    null=True,blank=True,related_name='Due_Rent')
    amount_paid= models.IntegerField()
    Balance= models.IntegerField()
    receipt_number =  models.CharField(default = random_string,max_length=50,editable=False)
    
    # receipt_number= models.CharField(max_length=50)

    PAY_TYPE_CHOICES=[
        ('Cleared','Cleared'),
        ('Balance','Balance')
    ]
    payment_status =models.CharField(choices=PAY_TYPE_CHOICES,default='Cleared',max_length=50)

    class Meta:
        verbose_name = ("payment")
        verbose_name_plural = ("payment")

    def __str__(self):
        return f'{self.tenant} - {self.contract}-{self.Balance}'

    def get_absolute_url(self):
        return reverse("Contract_detail", kwargs={"pk": self.pk})





    
    
