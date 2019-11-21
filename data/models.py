from django.db import models



class High_school(models.Model):
    """
    high school data
    """
    name = models.CharField(name='Name', max_length = 20, primary_key=True)
    location_lat = models.DecimalField(name = 'location_lat', decimal_places=8, max_digits= 10)
    location_long = models.DecimalField(name = 'location_long', decimal_places=8, max_digits= 10)


    class Meta:
        verbose_name = 'high_school'
        verbose_name_plural = 'high_school'


class College(models.Model):
    """d
    college data
    """

    CATEGORY = (
        ('0', 'America East Conference'),
        ('1', ''),
        ('2', ''),
        ('3', ''),
        ('4', ''),
        ('5', ''),
        ('6', ''),
        ('7', ''),
        ('8', ''),
        ('9', ''),
        ('10', ''),
        ('11', ''),
        ('12', ''),
        ('13', ''),
        ('14', ''),
        ('15', ''),
        ('16', ''),
        ('17', ''),
        ('18', ''),
        ('19', ''),
        ('20', ''),
        ('21', ''),
        ('22', ''),
        ('23', ''),
        ('24', ''),

    )

    name = models.CharField(name='Name', max_length=20, primary_key=True)
    College_League = models.IntegerField(name = 'College League', choices=CATEGORY)

    class Meta:
        verbose_name = 'College'
        verbose_name_plural = 'College'


class Player(models.Model):
    """
    player data
    """

    CATEGORY = (
        (0, 'AMERICAN ATHLETIC'),
        (1, 'BIG EAST'),
        (2, 'PATRIOT'),
        (3, 'IVY'),
        (4, 'COLONIAL ATHLETIC ASSOCIATION'),
        (5, 'SOUTHERN'),
        (6, 'PAC-12'),
        (7, 'WAC'),
    )

    first_name = models.CharField(name='First Name', max_length=20)
    last_name = models.CharField(name='Last Name', max_length=20)
    height = models.DecimalField(name = 'Height', decimal_places=2, max_digits=4, null=True,blank=True)
    weight = models.IntegerField(name = 'Weight', null=True,blank=True)
    state = models.CharField(name = 'State/Country', max_length=20, null=True,blank=True)
    hometown = models.CharField(name='Hometown', max_length=20, null=True,blank=True)


    High_school = models.ForeignKey(High_school,name = 'High School', on_delete=models.CASCADE)
    Team = models.ForeignKey(College,name = 'College', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

class Record(models.Model):
    """
    record data
    """

    POSITION = (
        (0, 'Forward'),
        (1, 'Midfielder'),
        (2, 'Defender'),
        (3, 'Back'),
        (4, 'Goalkeeper'),
    )

    potential_strat = models.IntegerField(name = 'Potential Strats',  null=True,blank=True)
    GP = models.IntegerField(name = 'GP',  null=True,blank=True)
    GS = models.IntegerField(name = 'GS',  null=True,blank=True)
    is_starter = models.NullBooleanField(name = 'Is_starter', null = True)

    Position1 = models.IntegerField(name = 'Position1', choices=POSITION,null=True)
    Position2 = models.IntegerField(name = 'Position2', choices=POSITION,null=True)
    Position3 = models.IntegerField(name = 'Position3', choices=POSITION,null=True)

    Roster_Year = models.IntegerField(name = 'Roster_Year',null=True,blank=True)
    Year = models.IntegerField(name = 'Year', null=True,blank=True)
    Player_num = models.IntegerField(name = 'Player_num', null=True,blank=True)


    Player = models.ForeignKey(Player, name = 'Player', on_delete=models.CASCADE)
    College = models.ForeignKey(College, name = 'College', on_delete=models.CASCADE)

    bio_link = models.CharField(name='bio_link', max_length=50, null=True, blank=True)


    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Record'




class Accolade(models.Model):
    """
    college data
    """

    TYPE = (
        ('0', 'First Team'),
        ('1', 'Second Team'),
        ('2', 'Third Team'),
        ('3', 'Rookie Team'),
        ('4', 'Honorable Mention'),
        ('5', 'Freshman Team'),
    )


    Year = models.IntegerField(name = 'Year')
    Accolade = models.IntegerField(name='Accolade', choices=TYPE)

    Player = models.ForeignKey(Player, name = 'Player', on_delete=models.CASCADE)
    College = models.ForeignKey(College, name = 'College', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Accolade'
        verbose_name_plural = 'Accolade'
