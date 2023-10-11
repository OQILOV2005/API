from rest_framework import serializers
from .models import *

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'



class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



class TestimonialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'