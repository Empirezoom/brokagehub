from django.db import models


from django.utils import timezone
import random
import string


from django.core.validators import RegexValidator


# Create your models here.



class CompanyProfile(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    logo = models.TextField()
    favicon = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=50)


        
    def __str__(self):
            return self.name
    class Meta:
        db_table = 'CompanyProfile'
        managed = True
        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfile'

        
class Services(models.Model):
    title = models.CharField(max_length=50)
    item1 = models.CharField(max_length=50)
    item2 = models.CharField(max_length=50)
    item3 = models.CharField(max_length=50)
    item4 = models.CharField(max_length=50)



        
    def __str__(self):
            return self.title
    class Meta:
        db_table = 'Services'
        managed = True
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

class ChooseUs(models.Model):
    svg = models.TextField()
    title = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    delay = models.CharField(max_length=50,)
    



        
    def __str__(self):
            return self.title
    class Meta:
        db_table = 'ChooseUs'
        managed = True
        verbose_name = 'ChooseUs'
        verbose_name_plural = 'ChooseUs'

class Testimonial(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    delay = models.CharField(max_length=50,)
    



        
    def __str__(self):
        return self.author
    class Meta:
        db_table = 'Testimonial'
        managed = True
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'







def generate_reference_id():
    """Generate unique reference ID in format BRK######HUB"""
    numbers = ''.join(random.choices(string.digits, k=6))
    return f"BRK{numbers}HUB"

class Registration(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=20, blank=True, null=True,unique=True,)
    phone = models.CharField(
    max_length=15,
    unique=True,
    validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )]
    )
    email = models.EmailField(max_length=254,unique=True)
    ssn = models.CharField(
        max_length=11,
        unique=True,
        validators=[RegexValidator(
            regex=r'^\d{3}-\d{2}-\d{4}$',
            message="SSN must be in the format: XXX-XX-XXXX"
        )]
    )
    address = models.TextField()

    
    # File uploads
    id_front = models.FileField(upload_to='uploads/ids/')
    id_back = models.FileField(upload_to='uploads/ids/')
    w2_form = models.FileField(upload_to='uploads/tax/')

    # Consent
    idme_consent = models.BooleanField(default=True,verbose_name="ID.me Verification Consent")

    accept = models.BooleanField(default=False,verbose_name="accepted ")
    rejected = models.BooleanField(default=False,verbose_name="rejected")

    # System fields
    reference_id = models.CharField(max_length=12, unique=True, default=generate_reference_id)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Registration"
        verbose_name_plural = "Registrations"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reference_id}"
    
    @property
    def age(self):
        """Return human-readable time since registration"""
        now = timezone.now()
        diff = now - self.created_at
        
        total_seconds = int(diff.total_seconds())
        
        if total_seconds < 60:
            return "Just now"
        elif total_seconds < 3600:  # Less than 1 hour
            minutes = total_seconds // 60
            return f"{minutes} min{'s' if minutes > 1 else ''} ago"
        elif total_seconds < 86400:  # Less than 1 day
            hours = total_seconds // 3600
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif total_seconds < 2592000:  # Less than 30 days
            days = total_seconds // 86400
            return f"{days} day{'s' if days > 1 else ''} ago"
        elif total_seconds < 31536000:  # Less than 1 year
            months = total_seconds // 2592000
            return f"{months} month{'s' if months > 1 else ''} ago"
        else:
            years = total_seconds // 31536000
            return f"{years} year{'s' if years > 1 else ''} ago"