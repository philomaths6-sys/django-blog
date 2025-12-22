
from .models import Category,About,Social

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_about(request):
    about = About.objects.latest('updated')
    return dict(about=about)
    
    
    
    
def get_social(request):
    social= Social.objects.all()
    return dict(social=social)   