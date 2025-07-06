from django.contrib import admin
from . models import *



# admin.py

from django.utils.html import format_html



# Register your models here.

class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone']
    prepopulated_fields = {'slug':('name',)}
    

    def has_add_permission(self, request):
    # Prevent manual addition through admin
        return False

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id','title','item1','item2','item3','item4']
    

    def has_add_permission(self, request):
    # Prevent manual addition through admin
        return False

class ChooseUsAdmin(admin.ModelAdmin):
    list_display = ['id','title','item','svg','delay']
    
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id','author','text','delay']



# @admin.register(Registration)
# class RegistrationAdmin(admin.ModelAdmin):
#     list_display = ['reference_id', 'first_name', 'last_name','email', 'phone', 'idme_consent','age', 'created_at']
#     list_filter = ['created_at', 'idme_consent']
#     search_fields = ['reference_id', 'first_name', 'last_name', 'phone']
#     readonly_fields = ['reference_id', 'created_at', 'age']
#     ordering = ['-created_at']
    
#     fieldsets = (
#         ('System Information', {
#             'fields': ('reference_id', 'age', 'created_at')
#         }),
#         ('Personal Information', {
#             'fields': ('first_name', 'last_name', 'email','address', 'phone', 'ssn')
#         }),
        # ('Consent', {
        #     'fields': ('idme_consent',)
        # }),
#         ('Documents', {
#             'fields': ('id_front', 'id_back', 'w2_form')
#         }),
#     )
    
    # def has_add_permission(self, request):
    #     # Prevent manual addition through admin
    #     return False


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'reference_id', 'first_name', 'last_name', 'email', 
        'phone','idme_consent', 'age_display', 'accept','rejected','created_at'
    ]
    list_filter = ['created_at','idme_consent']
    search_fields = ['reference_id', 'first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['reference_id', 'created_at', 'age_display']
    
    fieldsets = (
        ('Reference Information', {
            'fields': ('reference_id', 'created_at', 'age_display')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'address', 'phone', 'email', 'ssn')
        }),
        ('Documents', {
            'fields': ('id_front', 'id_back', 'w2_form')
        }),
            ('Consent', {
            'fields': ('idme_consent','accept','rejected')
        }),
    )
    
    def age_display(self, obj):
        return obj.age
    age_display.short_description = 'Age'
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')


    def has_add_permission(self, request):
    # Prevent manual addition through admin
        return False
    










admin.site.register(CompanyProfile,CompanyProfileAdmin) 
admin.site.register(Services,ServicesAdmin) 
admin.site.register(ChooseUs,ChooseUsAdmin) 
admin.site.register(Testimonial,TestimonialAdmin) 




# Customize admin site
admin.site.site_header = "Brokage Hub Admin"
admin.site.site_title = "Brokage Hub Admin Portal"
admin.site.index_title = "Welcome to Brokage Hub Administration"