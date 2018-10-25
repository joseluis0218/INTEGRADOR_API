from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, max_length=100, null=False)
    email = models.EmailField(max_length=150, blank=False)
    token = models.CharField(max_length=200,blank=False)

    def __unicode__(self):
        return self.email

class Captura(models.Model):
    id_captura = models.AutoField(primary_key=True, max_length=100, null=False)
    fecha = models.DateTimeField('date published')
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Rostro(models.Model):
    id_rostro = models.AutoField(primary_key=True, max_length=100, null=False)
    intensidad_pix = models.IntegerField(blank=False)
    cantidad_pix = models.IntegerField(blank=False)
    estado = models.CharField(max_length=35, blank=False)
    id_captura = models.ForeignKey(Captura,on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

