from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
	"""Registers a new customer and saves the info to our database"""

	if request.method == 'POST':
		form = UserRegisterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,
				f'{username}, welcome! Your account was successfully created! You can now log in.')
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'accounts/register.html', {'form': form})


def logout_user(request):
	"""Grab the username before logging out for a personalised goodbye"""

	username = request.user
	logout(request)

	return render(request, 'accounts/logout.html', {'username': username})


@login_required
def profile(request):
	"""Displays the current user's profile page with the current information
	rendered, with the ability to edit and save profile changes
	"""

	if request.method == 'POST':
		user_update_form = UserUpdateForm(request.POST, instance=request.user)
		profile_update_form = ProfileUpdateForm(request.POST,
												request.FILES,
												instance=request.user.profile)
		if user_update_form.is_valid() and profile_update_form.is_valid():
			user_update_form.save()
			profile_update_form.save()
			messages.success(request, f'Profile updated!')
			return redirect('profile')

	else:
		user_update_form = UserUpdateForm(instance=request.user)
		profile_update_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'user_update_form': user_update_form,
		'profile_update_form': profile_update_form
	}

	return render(request, 'accounts/profile.html', context)
