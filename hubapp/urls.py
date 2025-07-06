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
]