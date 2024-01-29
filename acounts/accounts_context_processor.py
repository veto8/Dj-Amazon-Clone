from .models import Profile

def my_profile(request):
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        user_id = 1 
    profile = Profile.objects.get(user=user_id)
    return {'profile':profile}