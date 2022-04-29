from django.db import models
from django.utils import timezone



class Note(models.Model):
    #Se actualizeaza automat data si ora cand notitele au fost create sau actualizate
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    #pentru titlu sa am string-uri  max 100 caractere
    title = models.CharField(max_length=100)

    #pentru continut sa am multe stringuri
    content = models.TextField()
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    IMPORTANCE_CHOICES = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    
    #daca nu se alege nivelul importantei, by default va fi nivel 3 = low
    importance = models.IntegerField(choices=IMPORTANCE_CHOICES, default=3)

    #metoda care va salva notita
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()    #daca obiectul nu are in id,atunci se va considera un obiect creat
        self.updated_at = timezone.now()    #daca obiectul are deja un id, atunci se va considera un obiect updatat
        return super(Note, self).save(*args, **kwargs)

