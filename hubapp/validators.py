# # validators.py
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# import re

# def validate_unique_email(email):
#     """
#     Custom validator to check if email already exists
#     """
#     from .models import Registration
    
#     if Registration.objects.filter(email=email).exists():
#         raise ValidationError(
#             f"The email '{email}' is already registered. Please use a different email address.",
#             code='email_exists'
#         )

# def validate_unique_phone(phone):
#     """
#     Custom validator to check if phone number already exists
#     """
#     from .models import Registration
    
#     if Registration.objects.filter(phone=phone).exists():
#         raise ValidationError(
#             f"The phone number '{phone}' is already registered. Please use a different phone number.",
#             code='phone_exists'
#         )

# def validate_phone_format(phone):
#     """
#     Validate phone number format (US format)
#     """
#     # Remove all non-digit characters
#     phone_digits = re.sub(r'\D', '', phone)
    
#     # Check if it's a valid US phone number (10 digits)
#     # if not re.match(r'^\d{10}$', phone_digits):  
#     if not re.match(r'^\+?1?\d{9,15}$', phone_digits): # but I  used because of testing with other country
#         raise ValidationError(
#             "Please enter a valid 10-digit phone number.",
#             code='invalid_phone_format'
#         )

# def validate_ssn_format(ssn):
#     """
#     Validate SSN format (XXX-XX-XXXX)
#     """
#     ssn_pattern = r'^\d{3}-\d{2}-\d{4}$'
#     if not re.match(ssn_pattern, ssn):
#         raise ValidationError(
#             "Please enter SSN in the format XXX-XX-XXXX.",
#             code='invalid_ssn_format'
#         )

# def validate_file_size(file):
#     """
#     Validate uploaded file size (max 5MB)
#     """
#     max_size = 5 * 1024 * 1024  # 5MB in bytes
#     if file.size > max_size:
#         raise ValidationError(
#             f"File size must be less than 5MB. Current size: {file.size / (1024*1024):.1f}MB",
#             code='file_too_large'
#         )

# def validate_file_extension(file):
#     """
#     Validate file extension for uploaded documents
#     """
#     allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.gif']
#     file_extension = file.name.lower().split('.')[-1]
    
#     if f'.{file_extension}' not in allowed_extensions:
#         raise ValidationError(
#             f"File type not allowed. Please upload files with extensions: {', '.join(allowed_extensions)}",
#             code='invalid_file_type'
#         )