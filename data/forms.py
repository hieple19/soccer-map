from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):
    CHOICES = (
        ('Michael', 'Michael'),
        ('Jun', 'Jun'),
        ('Paul', 'Paul'),
    )
    CATEGORY = (
        ('0', 'Null'),
        ('1', 'America East Conference'),
        ('2', 'American Athletic Conference'),
        ('3', 'ASUN Conference'),
        ('4', 'Atlantic 10 Conference'),
        ('5', 'Atlantic Coast Conference'),
        ('6', 'Big East Conference'),
        ('7', 'Big South Conference'),
        ('8', 'Big Ten Conference'),
        ('9', 'Big West Conference'),
        ('10', 'Colonial Athletic Association'),
        ('11', 'Conference USA'),
        ('12', 'Horizon League'),
        ('13', 'Ivy League'),
        ('14', 'Metro Atlantic Athletic Conference'),
        ('15', 'Mid-American Conference'),
        ('16', 'Missouri Valley Conference'),
        ('17', 'Northeast Conference'),
        ('18', 'Pac-12 Conference'),
        ('19', 'Patriot League'),
        ('20', 'Southern Conference'),
        ('21', 'The Summit League'),
        ('22', 'Sun Belt Conference'),
        ('23', 'West Coast Conference'),
        ('24', 'Western Athletic Conference'),

    )

    POSITIONS = (
        (0, 'Null'),
        (1, 'Forward'),
        (2, 'Midfielder'),
        (3, 'Defender'),
        (4, 'Back'),
        (5, 'Goalkeeper'),
    )

    League = forms.CharField(widget=forms.Select(choices=CATEGORY))
    Positions = forms.CharField(widget=forms.Select(choices=POSITIONS))
    Year = forms.CharField(widget=forms.TextInput,required=False)
    All_Conference_Year = forms.CharField(widget=forms.TextInput,required=False)

    class Meta:
        model = Player
        fields = ('League','Positions','Year','All_Conference_Year')
