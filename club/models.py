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

class Club1player(models.Model):
    CHOICE1SPLAYER = (('1', 'karim_benzema'), ('2', 'eden_hazard'), ('3', 'marcelo_vieira'), ('4', 'gareth_bale'), ('5', 'eduardo_camavinga'),
                     ('6', 'vini_jr'), ('7', 'ferland_mendy'), ('8', 'luka_modric'), ('9', 'david_alaba'), ('10', 'toni_kroos'), ('11', 'thibaut_courtois'),
                     ('12', 'federico_valverde'), ('13', 'rodrygo'), ('14', 'isco'), ('15', 'marco_asensio'), ('16', 'casemiro'), ('17', 'dani_carvajal'),
                     ('18', 'luka_jovic'), ('19', 'nacho'), ('20', 'lucas_vazquez'), ('21', 'eder_militao'), ('22', 'dani_ceballos'), ('23', 'mariano'),
                     ('24', 'miguel_gutierrez'), ('25', 'jesus_vallejo'), ('26', 'andriy_lunin'), ('27', 'antonio_blanco'), ('28', 'toni_fuidias_ribera'),
                     ('29', 'luis_federico_lopez'), ('30', 'sergio_santos'))
    club1players = models.CharField(choices=CHOICE1SPLAYER, max_length=24, null=True, blank=False)
    class Meta:
        verbose_name_plural = "Real Madrid Players"
    def __str__(self):
        return "{}".format(self.club1players)

class Club2player(models.Model):
    CHOICE2SPLAYER = (('1', 'marc_andre'), ('2', 'neto'), ('3', 'inaki_pena'), ('4', 'sergino_dest'),
                      ('5', 'gerard_pique'),
                      ('6', 'ronald_aroujo'), ('7', 'clement_lenglet'), ('8', 'jordi_alba'), ('9', 'sergi_roberto'),
                      ('10', 'oscar_mingueza'), ('11', 'samuel_umtiti'),
                      ('12', 'eric_garcia'), ('13', 'sergio_busquets'), ('14', 'riqui_puig'), ('15', 'philippe_coutinho'),
                      ('16', 'pedri'), ('17', 'frenkie_de_jong'),
                      ('18', 'ousmane_demlele'), ('19', 'mempehis_depay'), ('20', 'ansu_fati'), ('21', 'yusuf_demir'),
                      ('22', 'martin_braithwaite'), ('23', 'luuk_de_jong'),
                      ('24', 'sergio_agğero'))
    club2players = models.CharField(choices=CHOICE2SPLAYER, max_length=24, null=True, blank=False)

    class Meta:
        verbose_name_plural = "Barcelona Players"

    def __str__(self):
        return "{}".format(self.club2players)