from django.contrib import admin
import math

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Sezione(models.Model):
    nome_sezione = models.CharField(max_length=80)
    descrizione = models.CharField(max_length=150, blank=True, null=True)
    logo_sezione = models.ImageField(blank=True, null=True)


    class Meta:
        verbose_name ="Sezione"
        verbose_name_plural = "Sezioni"

    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse("sezione_view", kwargs={"pk":self.pk})

    def get_last_discussions(self):
        return Discussione.objects.filter(sezione_appartenenza = self).order_by("-data_creazione")[:2]

    def get_number_of_posts_in_section(self):
        return Post.objects.filter(discussione__sezione_appartenenza=self).count()




class Discussione(models.Model):
    titolo= models.CharField(max_length=120)
    data_creazione = models.DateTimeField(auto_now_add = True)
    autore_discussione = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "discussioni")
    sezione_appartenenza = models.ForeignKey(Sezione,on_delete = models.CASCADE)




    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("visualizza_discussione", kwargs={"pk":self.pk})

    def get_n_pages(self):
        """
        Restituisce il numero di pagina presenti in una istanza di Discussione.
        math.ceil https://docs.python.org/3.6/library/math.html#math.ceil
        restituisce il numero intero successivo al float passato come parametro (es 3.1 ==> 4)
        o restituisce lo stesso numero se intero
        """
        posts_discussione = self.post_set.count()
        n_pagine = math.ceil(posts_discussione / 3)
        return n_pagine


    class Meta:
        verbose_name ="Discussione"
        verbose_name_plural = "Discussioni"

class Post(models.Model):
    autore_post = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "posts")
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add = True)
    discussione = models.ForeignKey(Discussione, on_delete = models.CASCADE)

    def __str__(self):
        return self.autore_post.username

    class Meta:
        verbose_name ="Post"
        verbose_name_plural = "Posts"
# Register your models here.
