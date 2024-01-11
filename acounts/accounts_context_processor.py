from .models import Profile

def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    return {'profile':profile}