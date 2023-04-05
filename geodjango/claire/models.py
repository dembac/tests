from django.db import models
from django.contrib.gis.db.models import PointField, MultiPointField, MultiPolygonField
class Adherent(models.Model):
     
    raisonsociale= models.CharField(max_length=45)
    name= models.CharField(max_length=45)
    prenom= models.CharField(max_length=45)
    adresse= models.CharField(max_length=100)
    codepostale=models.CharField(max_length=80)
    ville = models.CharField(max_length=45)
    numagresani=models.CharField(max_length=45)
    coorets=models.IntegerField()
    coorportable= models.IntegerField()
    email= models.CharField(max_length=100)
    siret= models.CharField(max_length=45)     
    class Meta:
        db_table="adherent"





class Statutlieudit(models.Model):
    libelle= models.CharField(max_length=45)
    class Meta:
        db_table="statutlieudit"

class Lieudit(models.Model):
    namelieudit= models.CharField(max_length= 45)
    geom= MultiPolygonField()
    lon=models.FloatField()
    lat=models.FloatField()
    surface=models.FloatField()
    idstatutlieudit = models.ForeignKey(Statutlieudit, on_delete=models.CASCADE)
    class Meta:
        db_table="lieudit"

class Statutclaire(models.Model):
    libelle= models.CharField(max_length=45)
    class Meta:
        db_table="statutclaire"

class Constatterrain(models.Model):
    etatclaire= models.CharField(max_length=45)
    date= models.DateField()
    observation= models.TextField()
    indicecondition= models.FloatField()
    class Meta:
        db_table= "constatterrain"

class Claire(models.Model):
    idlieudit= models.ForeignKey(Lieudit, on_delete=models.CASCADE)
    surface=models.FloatField()
    codehydro=models.CharField(max_length= 20)
    geomclai=MultiPolygonField()
    lon=models.FloatField()
    lat=models.FloatField()
    nature=models.CharField(max_length=45)
    numautorisationexploi= models.CharField(max_length=45)
    nameclaire=models.CharField(max_length= 45)
    densitehuitre= models.FloatField()
    dureeaffinage=models.FloatField()
    source= models.CharField(max_length=45)
    dateentree= models.DateField()
    datesortie= models.DateField()
    volume=models.FloatField()
    salinite= models.FloatField()
    quantbiomasse= models.FloatField()
    profondeur= models.FloatField()
    matieresuspension= models.FloatField()
    tempearature= models.IntegerField()
    dateacquisition= models.DateField()
    ph= models.FloatField()
    tauxsurvie= models.FloatField()
    gainmassejournalier= models.FloatField()
    poidsmoyinitial=models.FloatField()
    poidsmoyfinal= models.FloatField()
    idstatutclaire = models.ForeignKey(Statutclaire, on_delete=models.CASCADE)
    idconstatterrain = models.ForeignKey(Constatterrain, on_delete=models.CASCADE)
    class Meta:
        db_table="claire"


class Typeadherent(models.Model):
    libelle=models.CharField(max_length=45)
    idadherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    class Meta:
        db_table= "type_adherent"