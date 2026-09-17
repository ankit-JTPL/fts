from django.db import models

class Contact(models.Model):
    interest = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    marketing_consent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.full_name
    
    class Meta:
        db_table = "contact_detail"
        ordering  = ['full_name', 'interest','company','position','email','phone','message','marketing_consent']
        verbose_name= 'Contact Detail'

    


