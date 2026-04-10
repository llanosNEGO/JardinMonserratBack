from django.contrib import admin
from .models import Matricula


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'anio', 'grado', 'seccion', 'estado']
    list_filter = ['anio', 'estado', 'grado', 'seccion', 'fecha_matricula']
    search_fields = ['alumno__nombres', 'alumno__apellidos', 'alumno__dni']
    readonly_fields = ['fecha_matricula', 'created_at', 'updated_at']
    fieldsets = (
        ('Información de Matrícula', {
            'fields': ('alumno', 'grado', 'seccion', 'anio', 'estado')
        }),
        ('Observaciones', {
            'fields': ('observaciones',),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_matricula', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
