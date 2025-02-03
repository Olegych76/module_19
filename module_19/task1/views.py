from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game, News
from django.shortcuts import render

# Create your views here.


def platform_news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
        games_ = Game.objects.all()
        return render(request, 'fourth_task/games.html', {'games': games_})


def cart(request):
    return render(request, 'fourth_task/cart.html')


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif len(password) < 8:
            info['error'] = 'Пароль должен быть не менее 8 символов'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif Buyer.objects.filter(name=name).exists():
            info['error'] = 'Пользователь уже существует'
        else:
            Buyer.objects.create(name=name, balance=0.00, age=int(age))
            info['success'] = f'Приветствуем, {name}!'

    return render(request, 'fifth_task/registration_page.html', {'info': info})


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif len(password) < 8:
                info['error'] = 'Пароль должен быть не менее 8 символов'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=name).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=name, balance=0.00, age=int(age))
                info['success'] = f'Приветствуем, {name}!'
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', {'info': info})
