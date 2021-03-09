"""
Add tables to django admin
"""
from django.contrib import admin

from .models import Proteins, Motifs, ProteinMotifs

admin.site.register(Proteins)
admin.site.register(Motifs)
admin.site.register(ProteinMotifs)
