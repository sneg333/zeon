from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
#     """
#     Generic class-based view listing books on loan to current user.
#     """
#     model = BookInstance
#     template_name = 'catalog/bookinstance_list_borrowed_user.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')

        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def useroot(request):
    useroot = UserProfile.objects.all()
    context = {
        'useroot': useroot,

    }
    return render(request, '/', context)