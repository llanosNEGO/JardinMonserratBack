from django.contrib import admin
from .models import Grado, Seccion, Alumno


@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nivel', 'orden', 'activo']
    list_filter = ['nivel', 'activo']
    search_fields = ['nombre']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Información del Grado', {
            'fields': ('nombre', 'nivel', 'orden', 'activo')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Información de la Sección', {
            'fields': ('nombre', 'activo')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['apellidos', 'nombres', 'dni', 'nro_matricula', 'estado']
    list_filter = ['estado', 'created_at']
    search_fields = ['nombres', 'apellidos', 'dni', 'nro_matricula']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Información Personal', {
            'fields': ('nro_matricula', 'nombres', 'apellidos', 'dni', 'fecha_nacimiento')
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono')
        }),
        ('Información del Apoderado', {
            'fields': ('nombre_apoderado', 'telefono_apoderado', 'email_apoderado')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
