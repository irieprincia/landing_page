from django.db import models



class Contact(models.Model):
    email= models.EmailField(max_length=100)
    nom= models.CharField(max_length=200)
    prenom=models.CharField(max_length=200)
    numero_de_telephone=models.CharField(max_length=10)
    pays=models.CharField(max_length=100)

    class Meta:
        verbose_name="client"


    def __str__(self):
        return self.nom



class Registration(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    contacted=models.BooleanField(default=False)

    contact=models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.nom

    class Meta:
        verbose_name="inscription"
    

# Create your models here.
