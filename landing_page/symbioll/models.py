from django.db import models



class Contact(models.Model):
    email= models.EmailField(max_length=100)
    nom= models.CharField(max_length=200)
    prénom=models.CharField(max_length=200)
    numéro_de_téléphone=models.IntegerField(max_length=10)
    pays=models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name="client"



class Registration(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    contacted=models.BooleanField(default=False)

    contact=models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.nom

    class Meta:
        verbose_name="inscription"


# Create your models here.
