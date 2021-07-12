# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import CustomUserSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import AllowAny


# class CustomUserCreate(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, format='json'):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlacklistTokenUpdateView(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = ()

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm

# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Profile
from .permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer


class ProfileList(ListCreateAPIView):
    queryset =Profile.objects.all()
    serializer_class =ProfileSerializer


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset =Profile.objects.all()
    serializer_class =ProfileSerializer

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            profile_form = ProfileForm(request.POST)

            if form.is_valid() and profile_form.is_valid():
                form.save()
                user_name = form.cleaned_data['username']
                profile_form.save(user_name)
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/accounts')
        else:
            form = SignUpForm()
            profile_form = ProfileForm()

        return render(request, 'accounts/signup.html', {'form': form, 'profile_form': profile_form})
    else:
        return redirect('/accounts')


@login_required
def profile(request):
    return render(request, "accounts/profile.html")