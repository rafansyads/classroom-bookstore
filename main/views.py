import datetime
from main.models import BookEntry
from main.forms import BookEntryForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='main:login')
def show_main(request):
    context = [
        BookEntry(name='Classroom of the Elite Year 2, Volume 1', price=235000, description='Classroom of The Elite Year 2, Volume 1 is a light novel written by Syougo Kinugasa and illustrated by Shunsaku Tomose. This light novel is the sequel of Classroom of The Elite Year 1, Volume 1. The story continues with the main character, Kiyotaka Ayanokouji, and his friends in the second year of their high school life. The story is set in the Advanced Nurturing High School, where students are divided into four classes based on their academic performance. The story follows the students as they navigate the challenges of high school life and strive to achieve their goals. The light novel is filled with suspense, drama, and mystery, making it a must-read for fans of the genre.',
                  quantity=1, category='Light Novel / Manga', isbn_13='9781638581826', isbn_10='1638581827', published_date='2022-07-19', pages=480, language='English', weight=0.38, publisher='Airship', rating_star=0.0, rating_count=0, author='Syougo Kinugasa', time_added='2024-09-05 22:19:00', review_list={}, image=''),
        BookEntry(name='Classroom of the Elite Year 2, Volume 2', price=235000, description='Classroom of The Elite Year 2, Volume 2 is the continuation of the thrilling light novel series written by Syougo Kinugasa and illustrated by Shunsaku Tomose. In this volume, the story delves deeper into the complex dynamics of the Advanced Nurturing High School, where students are constantly tested both academically and socially. Kiyotaka Ayanokouji and his classmates face new challenges and adversaries as they navigate their second year. With unexpected twists and intense character development, this volume keeps readers on the edge of their seats. The intricate plot and suspenseful narrative make it a compelling read for fans of the series.',
                  quantity=1, category='Light Novel / Manga', isbn_13='9781638583370', isbn_10='1638583377', published_date='2022-08-30', pages=488, language='English', weight=0.38, publisher='Airship', rating_star=0.0, rating_count=0, author='Syougo Kinugasa', time_added='2024-09-10 19:54:00', review_list={}, image=''),
        BookEntry(name='Classroom of the Elite Year 2, Volume 3', price=245000, description='Classroom of The Elite Year 2, Volume 3 continues the captivating journey of Kiyotaka Ayanokouji and his classmates at the Advanced Nurturing High School. Written by Syougo Kinugasa and illustrated by Shunsaku Tomose, this volume explores the deeper intricacies of the school\'s competitive environment. As the students face new trials and tribulations, alliances are tested and secrets are revealed. The stakes are higher than ever, and the characters must navigate through a web of deception and strategy to come out on top. This volume is packed with suspense, drama, and unexpected twists that will keep readers eagerly turning the pages.',
                  quantity=1, category='Light Novel / Manga', isbn_13='9781638586425', isbn_10='1638583385', published_date='2022-12-15', pages=516, language='English', weight=0.40, publisher='Airship', rating_star=0.0, rating_count=0, author='Syougo Kinugasa', time_added='2024-09-10 20:00:00', review_list={}, image=''),
        BookEntry(name='Classroom of the Elite Year 2, Volume 4', price=245000, description='Classroom of The Elite Year 2, Volume 4 is the latest installment in the popular light novel series by Syougo Kinugasa and Shunsaku Tomose. In this volume, Kiyotaka Ayanokouji and his classmates face new challenges and obstacles as they navigate the competitive world of the Advanced Nurturing High School. With the stakes higher than ever, the students must rely on their wits and skills to outsmart their rivals and achieve their goals. Packed with suspense, intrigue, and unexpected twists, this volume is a must-read for fans of the series.',
                  quantity=1, category='Light Novel / Manga', isbn_13='9781638588177', isbn_10='1638588171', published_date='2023-03-21', pages=512, language='English', weight=0.40, publisher='Airship', rating_star=0.0, rating_count=0, author='Syougo Kinugasa', time_added='2024-09-10 20:05:00', review_list={}, image=''),
        BookEntry(name='And Then There Were None', price=125000, description='And Then There Were None is a mystery novel by Agatha Christie, widely considered her masterpiece and described by her as the most difficult of her books to write. It was first published in the United Kingdom by the Collins Crime Club on 6 November 1939, as Ten Little N',
                  quantity=1, category='Mystery / Thriller', isbn_13='9780062073488', isbn_10='0062073486', published_date='1939-11-06', pages=272, language='English', weight=0.25, publisher='HarperCollins', rating_star=0.0, rating_count=0, author='Agatha Christie', time_added='2024-09-10 20:10:00', review_list={}, image=''),
        BookEntry(name='The Daily Laws: 366 Meditations on Power, Seduction, Mastery, Strategy, and Human Nature', price=190000, description='The Daily Laws: 366 Meditations on Power, Seduction, Mastery, Strategy, and Human Nature is a book by Robert Greene, the author of The 48 Laws of Power, The Art of Seduction, The 33 Strategies of War, The 50th Law, and Mastery. The Daily Laws is a collection of 366 meditations, one for each day of the year, based on the timeless wisdom of Greene\'s previous works. Each meditation offers insights and strategies for navigating the complexities of power, seduction, mastery, strategy, and human nature. Whether you are seeking personal growth, professional success, or a deeper understanding of the world, The Daily Laws provides a daily dose of wisdom and inspiration to guide you on your journey.',
                  quantity=1, category='Self-Help', isbn_13='9780593299234', isbn_10='059329923X', published_date='2023-09-05', pages=432, language='English', weight=0.50, publisher='Penguin Books', rating_star=0.0, rating_count=0, author='Robert Greene', time_added='2024-09-10 20:15:00', review_list={}, image=''),
        BookEntry(name='The Art of War', price=160000, description='The Art of War is an ancient Chinese military treatise attributed to Sun Tzu, a military strategist, and philosopher. The text is composed of 13 chapters, each focusing on different aspects of warfare and strategy. The Art of War has been widely studied and applied in various fields beyond military strategy, including business, politics, and sports. Its timeless wisdom and practical insights continue to be relevant in the modern world, making it a classic work on strategy and leadership.',
                  quantity=1, category='Philosophy', isbn_13='9780141023816', isbn_10='0141023813', published_date='2005-11-01', pages=112, language='English', weight=0.08, publisher='Penguin Books', rating_star=0.0, rating_count=0, author='Sun Tzu', time_added='2024-09-10 20:20:00', review_list={}, image=''),
        BookEntry(name='The 48 Laws of Power', price=230000, description='The 48 Laws of Power is a practical guide to understanding power dynamics and mastering the art of persuasion. Written by Robert Greene, the book explores the timeless principles of power and influence that have shaped history and continue to impact the world today. Drawing on historical examples and psychological insights, Greene offers a comprehensive framework for navigating the complexities of power in various contexts. Whether you are a leader, entrepreneur, or student of human nature, The 48 Laws of Power provides valuable lessons and strategies for achieving your goals and influencing others.',
                  quantity=1, category='Self-Help', isbn_13='9780140280197', isbn_10='0140280197', published_date='2000-09-01', pages=452, language='English', weight=0.45, publisher='Penguin Books', rating_star=0.0, rating_count=0, author='Robert Greene', time_added='2024-09-10 20:25:00', review_list={}, image=''),
    ]
    
    new_books = BookEntry.objects.all().order_by('-time_added')
    context = list(new_books) + context

    for book in context:
        book.image = book.image_url()

    return render(request, "main.html", {'context': context})

def add_book_entry_form(request):
    form = BookEntryForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, 'add_book.html', context)

def show_xml(request):
    books = BookEntry.objects.all()
    data = serializers.serialize('xml', books)
    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    books = BookEntry.objects.all()
    data = serializers.serialize('json', books)
    return HttpResponse(data, content_type='application/json')

def show_xml_by_id(request, id):
    book = BookEntry.objects.filter(pk=id)
    data = serializers.serialize('xml', book)
    return HttpResponse(data, content_type='application/xml')

def show_json_by_id(request, id):
    book = BookEntry.objects.filter(pk=id)
    data = serializers.serialize('json', book)
    return HttpResponse(data, content_type='application/json')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
        form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')