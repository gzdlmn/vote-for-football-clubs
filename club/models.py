from django.db import models

# Create your models here.

class Club(models.Model):
    CHOICES = (('1', 'real_madrid'), ('2', 'barcelona'), ('3', 'manchester_united'), ('4', 'juventus'), ('5', 'cheslea'),
               ('6', 'paris_saint_german'), ('7', 'bayern_munich'), ('8', 'arsenal'), ('9', 'liverpool'), ('10', 'manchester_city'))
    club_name = models.CharField(choices=CHOICES, max_length=20, null=True, blank=False)
    class Meta:
        verbose_name_plural = "10 Most Popular Football Clubs"
    def __str__(self):
        return "{}".format(self.club_name)