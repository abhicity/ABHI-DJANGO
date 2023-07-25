from .models import SocialMedia

def links_data(request):
    links = SocialMedia.objects.all()
    data = {'links':links}
    return data