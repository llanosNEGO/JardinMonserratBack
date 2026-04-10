from django.contrib import admin
from .models import Estudiante, Matricula


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['numero_documento', 'apellidos', 'nombres', 'grado', 'email', 'activo']
    list_filter = ['grado', 'activo', 'fecha_creacion']
    search_fields = ['nombres', 'apellidos', 'numero_documento', 'email']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    fieldsets = (
        ('Información Personal', {
            'fields': ('tipo_documento', 'numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento')
        }),
        ('Información Académica', {
            'fields': ('grado', 'activo')
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono', 'email')
        }),
        ('Información del Acudiente', {
            'fields': ('nombre_acudiente', 'telefono_acudiente', 'email_acudiente')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'año_lectivo', 'estado', 'fecha_matricula']
    list_filter = ['año_lectivo', 'estado', 'fecha_matricula']
    search_fields = ['estudiante__nombres', 'estudiante__apellidos', 'estudante__numero_documento']
    readonly_fields = ['fecha_matricula', 'fecha_creacion', 'fecha_actualizacion']
    fieldsets = (
        ('Información de Matrícula', {
            'fields': ('estudiante', 'año_lectivo', 'estado', 'observaciones')
        }),
        ('Fechas', {
            'fields': ('fecha_matricula', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
