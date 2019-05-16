from django.db import models
import textwrap




class Machine(models.Model):
    number = models.CharField(max_length=255) #numero de serie

    date = models.DateTimeField(auto_now_add=True)

    #etat = models.CharField(max_length=255) # allumée ou pas
    ETAT = (
        ('running', "En cours d'utilisation"),
        ('on', 'En fonctionnement'),
        ('off', 'Eteinte'),
        ('hs', 'Hors Service')

    )
    etat = models.CharField(max_length=1, choices=ETAT)
    heures = models.CharField(max_length=255) # total dheures de fonctionnement
    fabricant = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)
    #batiment = models.CharField(max_length=255)
    BATIMENT = (
        ('B', 'B'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G-J', 'G-J'),
        ('H', 'H'),
        ('I', 'I'),

    )
    batiment = models.CharField(max_length=1, choices=BATIMENT)
    historique = models.CharField(max_length=255)

    identifiant = models.CharField(max_length=255)

    type = models.CharField(max_length=255)


    class Meta:
        ordering = ['number', ]

    def __str__(self):
        return self.number

class Probleme(models.Model):
    nom = models.CharField(max_length=255)
    #pub_date = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)

    machine = models.CharField(max_length=255)
    BATIMENT = (
        ('B', 'B'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),

    )
    batiment = models.CharField(max_length=1, choices=BATIMENT)

    description = models.TextField()
    #body = textwrap.fill(str(body), width=30)
    SOLVED = (
        ('A', 'Accepté'),
        ('N', 'Nié'),
        ('NT','Non traité'))

    resolution = models.CharField(max_length=1, choices=SOLVED)



    class Meta:
        ordering = ['-date', ]

    def __str__(self):
        return self.resolution + " - " + self.batiment + " - " +self.nom


