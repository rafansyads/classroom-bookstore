# Classroom Bookstore

A book e-commerce to coloring your knowledge (this is a trial repo for assignments)


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Questions (to sneakpeek)](#questionssneakpeek)

## Installation

Step-by-step instructions on how to get the development environment running.

```bash
# Clone the repository
git clone https://github.com/rafansyads/classroom-bookstore.git

# Navigate to the project directory
cd yourproject

# Install dependencies
pip install -r requirements.txt

# Run the application
python manage.py runserver
```
## Usage

As of now, the usage to the project is limited to only viewing blank (or maybe brief) ```main.html``` file.

## Contributing

Guidelines for contributing to the project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (```git push origin feature-branch```).
6. Open a pull request.

## License

This project is license-free.

## Contact

rafansyads - rafansya2005@gmail.com

Project Link: https://github.com/rafansyads/classroom-bookstore

## Questions (to sneakpeek)

**|| All the questions and the answers are only available in Indonesian ||** 
- [TM2 Questions](#tm2-questions)
- [TM3 Questions](#tm3-questions)
- [Linked Images: TM3](#tm3-images)

### TM2 Questions
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

> * Step 1: Membuat setup virtual environment menggunakan Python Virtual Environment dengan command di Terminal `python -m venv env` atau `python -m virtualenv env`. Setelahnya, aktifkan virtual environment dengan command `env\Scripts\activate`.
>
> * Step 2: Membuat project Django yang dijalankan di virtual environment dengan command (setelah venv diaktifkan) `django-admin startproject <nama_proyek>` (catatan: nama_proyek diisi, dalam konteks ini, sesuai nama directory, dalam konteks ini adalah `classroom_bookstore`).
>
> * Step 3: Membuat aplikasi Django dengan command `django-admin startapp <nama_proyek>` (catatan: nama_proyek diisi, dalam konteks ini, `main`) dan menambahkan `main`, localserver, dan PWS web deployment address di list `ALLOWED_HOST` di `setting.py`.
>
> * Step 4: Membuat model aplikasi di `models.py` yang ada di aplikasi `main`, dengan memasukkan Class(es) yang dibutuhkan. Seperti contohnya, dalam aplikasi ini, memasukkan Class bernama `BookEntry` dengan berbagai atribut beserta Fields' yang dibutuhkan.
>> `Code Entry:`
>> ```bash
>> ...
>> class BookEntry(models.Model):
>> # Menampilkan 3 entri wajib dari class BookEntry yang diminta
>>    name = models.CharField(max_length=100)
>>    price = models.IntegerField()
>>    description = models.TextField()
>> 
>> # Entri selanjutnya
>> ...
>
> * Step 5: Melakukan migrasi dan membuat dan menambah URL dan View. Memulai migrasi setiap adanya perubahan models yang terjadi di `models.py` dengan command `python manage.py makemigrations` dan dilanjutkan dengan `python manage.py migrate`. Setelahnya, menambahkan URL di `urls.py` di aplikasi (konteks: `main`) dan di project (konteks: `classroom_bookstore`) dengan menambahkan URL di kedua `urls.py` tersebut. URL tersebut akan dipakai untuk menampilkan request yang akan ditampilkan dari `views.py`. `views.py` dapat ditambahkan method `show_main` untuk menampilkan berbagai atribut yang diinginkan dengan sekaligus `import render` dalam views.py yang akan ditampilkan di HTML (konteks: `main.html`).
>> `Code Entry (urls.py di main)`
>> ```bash
>> from django.urls import path
>> from main.views import show_main
>> 
>> app_name = 'main'
>> 
>> urlpatterns = [
>>     path('', show_main, name='show_main'), # Setup for Django's main app
>> ]
>> ```
>
>> `Code Entry (urls.py di project)`
>> ``` bash 
>> from django.contrib import admin
>> from django.urls import path, include
>> 
>> urlpatterns = [
>>     path('admin/', admin.site.urls), # Direct requests to Django admin interface
>>     path('', include('main.urls')), # Direct requests to main's urls.py
>> ]
>> ```
>
>> `Code Entry (views.py)`
>> ```bash
>> from django import render
>> 
>> # Create your views here.
>> def show_main(request):
>>     context = {
>>         'name' : 'Classroom of The Elite Year 2, Volume 2',
>>         'price': 235000,
>>         ...
>>     }
>> # Render the request to the main.html as the given template with the context database to view
>> return render(request, 'main.html', context)
>> ```
>
> * Step 6: Melakukan test server lewat localserver venv dan commit, deployment di PWS dan/atau Github. Jangan lupa untuk menambahkan URL deployment di `ALLOWED_HOSTS`.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
>
> * `# Client Request -> urls.py -> views.py -> models.py -> views.py -> templates (HTML) -> Client Response`
>
> **Penjelasan:**
>
> * urls.py: Menerima request dari client dan menentukan view yang akan dipanggil berdasarkan URL yang diambil.
> * views.py: Mengambil data dari model (jika diperlukan), memproses data (pada step ketiga), dan mengembalikan response (pada step kelima dan lewat HTML).
> * models.py: Berinteraksi dengan database untuk mengambil atau menyimpan data.
> * templates (HTML): Menampilkan data yang diproses oleh view dalam format HTML yang dikirim kembali ke client. Templates HTML dapat berupa aplikasi main atau yang lainnya.


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
> * Melacak perubahan sumber code selama pengembangan, baik dalam level local, global, maupun lewat aplikasi pihak ketiga secara online, seperti GitHub dan GitLab;
> * Memungkinkan kolaborasi bersama dalam satu project;
> * Memungkinkan adanya branch baru untuk perbaikan minor/major atau fitur baru tanpa mengganggu branch (kode) utama;
> * Memudahkan restore code jika terjadi kesalahan pada suatu stage/commit tertentu; dan
> * Memungkinkan merge, baik untuk pull maupun push request, perubahan dari berbagai branch.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
> * Terdapat fitur bawaan seperti autentikasi, admin panel, Object-Relational Mapping (ORM), dan routing secara otomatis;
> * Dokumentasi lengkap, penggunaan luas, dan komunitas besar; 
> * Django menyediakan API yang juga mudah digunakan untuk operasi CRUD (Create, Read, Update, Delete); dan
> * Convention over Configuration (sehingga memudahkan pengguna baru untuk memahami alur pekerjaan aplikasi).

5. Mengapa model pada Django disebut sebagai ORM?
> * Django menggunakan konsep OOP dan relasi untuk menghubungkan aplikasi dengan database secara relasional tanpa menggunakan SQL sehingga memudahkan pengembang untuk bekerja dengan menuliskan Object tanpa SQL. Django menyediakan API yang juga mudah digunakan untuk operasi CRUD (Create, Read, Update, Delete)

### TM3 Questions
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
> * Data delivery diperlukan dalam pengimplementasian sebuah platform untuk memastikan bahwa data dapat dikirim dan diterima dengan benar antara berbagai komponen sistem. Data delivery memungkinkan delivery data yang sama seperti data yang diterima (seperti kalanya di `forms.py`). Data delivery juga memungkinkan integrasi dengan layanan eksternal, seperti third-party APIs: untuk fungsionalitas platform dll.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
> **JSON lebih baik dibandingkan XML dalam banyak kasus**
>
> **Alasan:** 
> * JSON lebih ringan, lebih mudah dibaca oleh manusia, dan menggunakan sintaks yang lebih sederhana dan lebih mudah di-parse oleh mesin sehingga lebih efisien.
> * JSON juga lebih mudah diintegrasikan (kompatibel) dengan JavaScript, yang merupakan bahasa pemrograman utama untuk pengembangan web.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
> * Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dikirimkan melalui form. Method ini memeriksa apakah data yang dimasukkan sesuai dengan aturan validasi yang telah ditentukan dalam form. Validasi dilakukan dengan kesesuaian data, termasuk data type, dengan isi field yang diminta (contoh: input `String` **bukan whitespace** untuk `CharField` atau `TextField`). **Jika data valid**, method ini akan mengembalikan nilai `True`, dan data yang telah divalidasi dapat diakses melalui atribut `cleaned_data`. **Otherwise**, method ini akan mengembalikan nilai `False` dan pesan kesalahan akan disimpan dalam atribut `errors`. Kita membutuhkan method ini untuk memastikan bahwa data yang diterima oleh aplikasi adalah data yang benar dan sesuai dengan aturan yang telah ditentukan, sehingga dapat mencegah kesalahan dan potensi masalah keamanan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
> * **Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF)**. `csrf_token` adalah token unik (`checksum`) yang dihasilkan oleh server dan disertakan dalam setiap form yang dikirimkan oleh pengguna. Token ini diverifikasi oleh server saat menerima permintaan untuk memastikan bahwa permintaan tersebut berasal dari sumber yang sah. Setiap entri yang dilakukan dan sudah di-`POST` akan diamankan melalui `csrf_token`. Jika kita tidak menambahkan `csrf_token` pada form, penyerang dapat memanfaatkan kelemahan ini dengan mengirimkan permintaan palsu atas nama pengguna yang sah, yang dapat mengakibatkan tindakan yang tidak diinginkan seperti perubahan data atau pencurian informasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
> * Membuat template `base.html` di `templates` di `ROOT_DIR`. Hal ini dilakukan untuk memberikan template kepada laman-laman web HTML lainnya, termasuk di dalamnya `add_book.html` yang diproses melalui `forms.py`:
> ```html
> {% load static %}
> <!DOCTYPE html>
> <html lang="en">
>  <head>
>    <meta charset="UTF-8" />
>     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
>     {% block meta %} {% endblock meta %}
>  </head>
>
>  <body>
>     {% block content %} {% endblock content %}
>  </body>
> </html>
> ```
> * Selanjutnya `base.html` tersebut di-extend di seluruh laman HTML web lainnya: (dalam konteks ini `main.html` dan `add_book.html` dengan sintaks `{% extends base.html %}`)
> * Menambahkan **UUID** dengan `import uuid` di `models.py` untuk menambah keamanan dan sebagai id untuk setiap data yang masuk lewat `add_book.html` (`forms.py`) dan ditampilkan lewat `String` id untuk `primary key`-nya `pk`-id entrinya itu sendiri (dapat ditampilkan nanti lewat JSON/XML).
> * Membuat `forms.py`:
> ```python
> from django import forms
> from django.forms import ModelForm
> from main.models import BookEntry # import the BookEntry model from models.py
> 
> class BookEntryForm(ModelForm):
>     class Meta:
>         model = BookEntry # BookEntry model from models.py
> 
>         fields = [ # list of fields to be included in the form
>             'name', 'price', 'description',
>         # Next entries go here
>         ]
> ...
>         widgets = { # dictionary of widgets to customize the form fields
>             'published_date': forms.DateInput(attrs={'type': 'date'}),
>             'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
>         }
>         # Next features to the forms.py such as helper etc.
> ...
> ```
> * Membuat method untuk validasi entries form dari `forms.py`: `add_book_entry_form(request)` dan menambah `import redirect` di `views.py`
> ```python
> from django.shortcuts import render, redirect 
> ...
> def add_book_entry_form(request):
>     form = BookEntryForm(request.POST or None, request.FILES or None)
> 
>     if form.is_valid() and request.method == 'POST':
>         form.save()
>         return redirect('main:show_main')
> 
>     context = {'form': form}
>     return render(request, 'add_book.html', context) # redirect to add_book.html with add_book_entry_form(request)
> ```
> * Memodifikasi method `show_main` agar sekaligus menampilkan entry baru yang akan muncul di list books di `main.html`
> ```python
>     new_books = BookEntry.objects.all().order_by('-time_added') # Add and sort the newest books by the time added (descending from the latest entries)
>     context = list(new_books) + context
> ```
> * Men-direct URL `add_book.html` dengan `forms.py` untuk dimasukkan ke dalam `urls.py` di directory `main`
> ```python
> from main.views import show_main, add_book_entry_form, show_json, show_xml, show_xml_by_id, show_json_by_id
> ...
> path('add-book', add_book_entry_form, name='add_book'), # Adding url ./add-book
> ```
> * Menambahkan direction to add_book.html dan show new entries di `main.html`.
> * Menambahkan methods untuk show book entries lewat XML dan JSON (better) di `views.py` dengan berbagai method berikut:
> ```python
> # Import HttpResponse and serializers to further show XML and JSON (can be used for other features)
> from django.http import HttpResponse
> from django.core import serializers
> ...
> def show_xml(request):
>     books = BookEntry.objects.all()
>     data = serializers.serialize('xml', books)
>     return HttpResponse(data, content_type='application/xml')
> 
> def show_json(request):
>     books = BookEntry.objects.all()
>     data = serializers.serialize('json', books)
>     return HttpResponse(data, content_type='application/json')
> 
> def show_xml_by_id(request, id):
>     book = BookEntry.objects.filter(pk=id)
>     data = serializers.serialize('xml', book)
>     return HttpResponse(data, content_type='application/xml')
> 
> def show_json_by_id(request, id):
>     book = BookEntry.objects.filter(pk=id)
>     data = serializers.serialize('json', book)
>     return HttpResponse(data, content_type='application/json')
> ```
> * Untuk show JSON dan XML, direct URL di `urls.py` di `main` directory
> ```python
> ...
>     path('json/', show_json, name='show_json'),
>     path('xml/', show_xml, name='show_xml'),
>     path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
>     path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
> ...
> ```

## Linked Images: TM3
* https://drive.google.com/file/d/11AqnKIrWYsxieNMhu5dRm2mpgZ4GpFqQ/view?usp=sharing, 
* https://drive.google.com/file/d/1AOkX5NTui4nFmU7RpESOFvzGTiwqVRq8/view?usp=sharing, 
* https://drive.google.com/file/d/1o8YNXCkz7onn0F362bkC3zWpsVt3xOKh/view?usp=sharing, 
* https://drive.google.com/file/d/1zLFi5q2OAdktVpvBiphAvAFkHYBM92tx/view?usp=sharing