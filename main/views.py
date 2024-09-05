from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Classroom of The Elite Year 2, Volume 2',
        'price': 235000,
        'description': 'Classroom of The Elite Year 2, Volume 1 is a light novel written by Syougo Kinugasa and illustrated by Shunsaku Tomose. This light novel is the sequel of Classroom of The Elite Year 1, Volume 1. The story continues with the main character, Kiyotaka Ayanokouji, and his friends in the second year of their high school life. The story is set in the Advanced Nurturing High School, where students are divided into four classes based on their academic performance. The story follows the students as they navigate the challenges of high school life and strive to achieve their goals. The light novel is filled with suspense, drama, and mystery, making it a must-read for fans of the genre.',
        'quantity': 1,
        'category': 'Light Novel / Manga',
        'isbn_13': '9781638583370',
        'isbn_10': '1638583377',
        'published_date': '2022-08-30',
        'pages' : 488,
        'language': 'English',
        'weight': 0.38,
        'publisher' : 'Seven Seas Entertainment',
        'rating_star': 0.0,
        'rating_count': 0,
        'author': 'Syougo Kinugasa',
        'time_added': '2024-09-05 22:19:00',
        'review_list': {},
    }

    return render(request, "main.html", context)
