from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializres import *

@api_view(['GET'])
def get_banner_view(request):
    banner = Banner.objects.last()
    ser = BannerSerializers(banner)
    return Response(ser.data)


@api_view(['GET'])
def get_teams_views(request):
    team = Team.objects.all()
    ser = TeamSerializers(team,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_skill_views(request):
    skill = Skill.objects.all()
    ser =SkillSerializers(skill,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_service_views(request):
    service = Service.objects.all()
    ser =ServiceSerializers(service,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_about_views(request):
    about = About.objects.all()
    ser =AboutSerializers(about,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_testimonial_views(request):
    testimonial = Testimonial.objects.all()
    ser =TestimonialSerializers(testimonial,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_image_views(request):
    imgage = Image.objects.all()
    ser =ImageSerializers( imgage,many=True)
    return Response(ser.data)


@api_view(['POST'])
def create_contact_views(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        new_contacts = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        ser = ContactSerializers(new_contacts)
        return Response(ser.data)