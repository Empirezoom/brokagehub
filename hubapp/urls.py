from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    # path('later',views.later,name='later'),

    # path('form', views.registration_form, name='form'),
    # path('success/', views.success_view, name='success'),

    path('register/', views.registration_view, name='register'),
    path('success/', views.success_view, name='success'),
    path('check-email/', views.check_email, name='check_email'),
    path('check-phone/', views.check_phone, name='check_phone'),

    path('brk-not-enter/',views.activity_admin_tay,name='minister'),
    path('detail/<str:reference_id>/<str:id>',views.detail,name='detail'),




    path('payroll/', views.payroll, name='payroll'),
    path('book-keeping_&_accounting/', views.book_keeping, name='book_keeping'),
    path('financial-consulting/', views.financial, name='financial'),
    path('tax-planning_&_preparation/', views.tax_planning, name='tax_planning'),
    path('business_incorporation_services/', views.business_incorporation, name='business_incorporation'),
    path('compliance_&_reporting/', views.compliance, name='compliance'),

  
]