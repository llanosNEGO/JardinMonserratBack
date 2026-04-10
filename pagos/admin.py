from django.contrib import admin
from .models import Pago, ConceptoPago


@admin.register(ConceptoPago)
class ConceptoPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'monto', 'es_mensualidad', 'activo']
    list_filter = ['es_mensualidad', 'activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    fieldsets = (
        ('Información del Concepto', {
            'fields': ('nombre', 'descripcion', 'monto', 'es_mensualidad', 'activo')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'concepto', 'monto', 'fecha_pago', 'metodo_pago', 'estado']
    list_filter = ['estado', 'metodo_pago', 'fecha_pago', 'concepto']
    search_fields = ['estudiante__nombres', 'estudiante__apellidos', 'estudiante__numero_documento', 'referencia']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    fieldsets = (
        ('Información del Pago', {
            'fields': ('estudiante', 'concepto', 'monto', 'metodo_pago', 'estado')
        }),
        ('Comprobante y Referencia', {
            'fields': ('comprobante', 'referencia', 'observaciones'),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_pago', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
