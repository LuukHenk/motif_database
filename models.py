"""
Database models
Based on: https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-many-relationships
"""
from django.db import models

class Motifs(models.Model):
    """ Saved motif sequences """
    sequence = models.CharField(
        max_length=1000,
        unique=True,
        primary_key=True
    )
    description = models.TextField(
        max_length=2000,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.sequence

class Proteins(models.Model):
    """ Saved protein sequences and its motifs """
    label = models.CharField(
        max_length=100,
        unique=True,
        primary_key=True
    )
    full_name = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    sequence = models.TextField(
        max_length=10000
    )
    description = models.TextField(
        max_length=2000,
        blank=True,
        null=True
    )
    motifs = models.ManyToManyField(
        Motifs,
        through='ProteinMotifs'
    )

    def __str__(self):
        return self.label

class ProteinMotifs(models.Model):
    """ Motifs per protein """
    protein = models.ForeignKey(
        Proteins,
        on_delete=models.CASCADE
    )
    motif = models.ForeignKey(
        Motifs,
        on_delete=models.CASCADE
    )
    site = models.CharField(
        max_length=100
    )
