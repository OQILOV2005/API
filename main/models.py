from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Sarlavha',blank=False)
    text = models.TextField(verbose_name='Text')
    img = models.ImageField(upload_to='banner_photo/',verbose_name='Banner-photo/')

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=255, verbose_name='Sarlavha',blank=False)
    text = models.TextField(verbose_name='Text')
    img = models.ImageField(upload_to='skill_photo/',verbose_name='Skill-photo/')

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ism',blank=False)
    job = models.CharField(max_length=25, verbose_name='Kasbi')
    img = models.ImageField(upload_to='team-photo/',verbose_name='Team-photo/')
    twitter = models.CharField(max_length=25, verbose_name='Twitter')
    linkedin = models.CharField(max_length=25, verbose_name='Linkedin')
    facebook = models.CharField(max_length=25, verbose_name='Facebbok')
    instagram = models.CharField(max_length=25, verbose_name='Instagram')

    def __str__(self):
        return self.name


class Image(models.Model):
    img = models.ImageField(upload_to='about-photo/', verbose_name="About-photo")


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Sarlavha', blank=False)
    description = models.CharField(max_length=255, verbose_name='Tasnif', blank=False)
    text = models.TextField(verbose_name='Text')
    img = models.ManyToManyField(to=Image)

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Xizmat-turi', blank=False)
    text = models.CharField(max_length=255, verbose_name='Batafsil')
    icon = models.ImageField(upload_to='service_icon/', verbose_name='Service_icon')

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name='Mijoz Ism', blank=False)
    comment = models.CharField(max_length=255, verbose_name='Izoh')
    avatar = models.ImageField(upload_to='testimonial_icon/', verbose_name='Testimonial_icon')

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=' Ism')
    last_name = models.CharField(max_length=255, verbose_name=' Ism')
    email = models.CharField(max_length=255, verbose_name='elektron pochta')
    subject = models.CharField(max_length=255, verbose_name='Maqsad')
    message = models.TextField( verbose_name='Xabar')

    def __str__(self):
        return self.first_name
from django.db import models

# Create your models here.
