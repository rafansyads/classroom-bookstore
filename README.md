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
- [TM4 Questions](#tm4-questions)
- [TM5 Questions](#tm5-questions)
- [TM6 Questions](#tm6-questions)
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

### TM4 Questions
1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
> * `HttpResponseRedirect()` adalah kelas yang digunakan untuk mengembalikan respons HTTP yang mengarahkan pengguna ke URL tertentu. URL lengkap diperlukan sebagai argumen seperti: 
> ```python
> ...
> def show_xml(request):
>     books = BookEntry.objects.all() # All books entries as XML content
>     data = serializers.serialize('xml', books) # Serialise the books content
>     return HttpResponse(data, content_type='application/xml') # Return HTTP from the serialised data to be linked as site/xml
> ...
> ```
> * `redirect()` adalah fungsi yang lebih sederhana dan fleksibel yang dapat menerima URL, nama view, atau bahkan objek model sebagai argumen. Fungsi ini akan mengonversi argumen yang diberikan menjadi URL yang sesuai. Contoh:
> ```python
> def add_book_entry_form(request):
>     form = BookEntryForm(request.POST or None, request.FILES or None)
>
>     if form.is_valid() and request.method == 'POST':
>         mood_entry = form.save(commit=False)
>         mood_entry.user = request.user
>         mood_entry.save()
>         return redirect('main:show_main') # Redirect to main menu html
> ```

2. Jelaskan cara kerja penghubungan model Product dengan User!
> * Penghubungan model `Product` dengan `User` dilakukan dengan menggunakan `ForeignKey`. Ini memungkinkan setiap entri produk dikaitkan dengan pengguna tertentu. Berikut adalah contoh cara menghubungkan model `Product` dengan `User`:
> ````python
> from django.auth.models import User
> from django.db import models
>
> class Product(models.Model):
>     user = models.ForeignKey(User, on_delete=models.CASCADE) # Linked user
>     name = models.CharField(max_length=100)
>     price = models.DecimalField(max_digits=10, decimal_places=2)
>     description = models.TextField()
>     # More attributes go here
>     ...
> ````
> * Dalam contoh ini, setiap produk memiliki kolom `user` yang merujuk ke pengguna yang membuat atau memiliki produk tersebut. `on_delete=models.CASCADE` berarti jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
> * **Authentication** adalah proses verifikasi identitas pengguna. *Authentication* biasanya dilakukan dengan memeriksa credentials seperti username dan password. Setelah memasukkan credentials, maka user akan masuk sesuai dengan data, identitas, dan **authorization**-nya masing-masing.
> * **Authorization** adalah proses menentukan hak akses pengguna setelah mereka terautentikasi. *Authorization* menentukan apa yang dapat dan tidak dapat dilakukan oleh pengguna. *Authorization* dapat dilakukan dengan mengeset secara manual dari admin dan/atau sistem (seperti Django).
> * Saat pengguna login, proses ***authentication*** dilakukan untuk memverifikasi identitas pengguna. Jika berhasil, Django akan membuat sesi untuk pengguna tersebut dan menyimpan informasi sesi di cookies.
> Django mengimplementasikan authentication menggunakan `django.contrib.auth` yang menyediakan model `User`, form login, dan mekanisme backend untuk memverifikasi credentials. ***Authorization*** diimplementasikan melalui izin (permissions) dan grup (groups) yang dapat dikaitkan dengan pengguna.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
> * Django mengingat pengguna yang telah login dengan menggunakan sesi (sessions). Saat pengguna berhasil login, Django membuat sesi baru dan menyimpan ID sesi di cookies. Setiap kali pengguna membuat permintaan, cookies dikirim kembali ke server untuk mengidentifikasi pengguna.
> * Cookies juga digunakan untuk menyimpan preferensi pengguna, melacak aktivitas pengguna, dan menyimpan data sementara lainnya. Namun, tidak semua cookies aman digunakan. Cookies dapat rentan terhadap serangan seperti ***Cross-Site Scripting (XSS)*** dan ***Cross-Site Request Forgery (CSRF)***. Oleh karena itu, penting untuk mengamankan cookies dengan menggunakan atribut keamanan seperti `HttpOnly`, `Secure`, dan `SameSite`.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
> * Membuat form register dan login HTML terlebih dahulu, dan merestriksi akses main menu dengan `@login_required(login_url='/login')`;
> * Selanjutnya, membuat methods untuk melakukan register dan login di `views.py`;
> * Logout dibuat dengan redirect ke form login (basically keluar dari main menu HTML);
> * Menambahkan *cookies* sebagai informasi data pengguna. Hal ini dilakukan untuk mendata informasi *login* dan *logout* pengguna. *Cookies* seharusnya diamankan dengan menggunakan atribut kemanan (lihat no. 4);
> * *Last but not least*, menghubungkan `Product` dengan `User` dengan menambahkan atribut `user` di `Models`. Atribut `User` juga bisa di-set *default* dengan menambahkan parameter `default=...` atau mengesetnya sendiri ketika melakukan *migrations*.

## TM5 Questions
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
> Urutan prioritas CSS selector ditentukan oleh spesifisitas. Spesifisitas dihitung berdasarkan jenis selector yang digunakan. Berikut adalah urutan prioritas dari yang tertinggi ke terendah:
> * **Inline Styles:** CSS yang ditulis langsung di atribut style pada elemen HTML. Contoh: `<div style="color: red;">`.
> * **ID Selector:** Selector yang menggunakan ID elemen. Contoh: `#header`.
> * **Class, Attribute, dan Pseudo-class Selectors:** Selector yang menggunakan class, atribut, atau pseudo-class. Contoh: `.container`, `[type="text"], :hover`.
> * **Element dan Pseudo-element Selectors:** Selector yang menggunakan nama elemen atau pseudo-element. Contoh: `div, ::before`.
> Jika dua selector memiliki spesifisitas yang sama, maka yang terakhir didefinisikan dalam CSS akan diambil.
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
> Responsive design adalah konsep penting dalam pengembangan aplikasi web karena memastikan bahwa aplikasi dapat diakses dan digunakan dengan baik di berbagai perangkat dengan ukuran layar yang berbeda. Ini meningkatkan pengalaman pengguna dan memastikan aksesibilitas yang lebih luas. Contohnya: laptop dengan layar 16:9, 16:10, 3:4 dan juga mobile dengan layar 16:9, 18:9, 21:9, dan ukuran layar absurd lainnya.
> * **Sudah Menerapkan:** Twitter, yang menyesuaikan tata letak dan ukuran elemen berdasarkan ukuran layar.
> * **Belum Menerapkan:** Situs web lama yang hanya dirancang untuk tampilan desktop dan tidak menyesuaikan dengan layar perangkat mobile.
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
> **Margin**: Ruang di luar border elemen. Digunakan untuk memberikan jarak antara elemen.
> ```css
> .example {
>    margin: 20px;
> }
> ```
> **Border**: Garis yang mengelilingi padding dan konten elemen.
> ```css
> .example {
>     border: 2px solid black;
> }
> ```
> **Padding**: Ruang di dalam border elemen, antara border dan konten.
> ```css
> .example {
>    padding: 10px;
> }
> ```
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
> **Flexbox:** Layout model yang digunakan untuk mengatur elemen dalam satu dimensi (baris atau kolom). Berguna untuk membuat layout yang fleksibel dan responsif.
> ```css
> .container {
>     display: flex;
>     justify-content: center;
>     align-items: center;
> }
> ```
> **Grid Layout:** Layout model yang digunakan untuk mengatur elemen dalam dua dimensi (baris dan kolom). Berguna untuk membuat layout yang kompleks dan responsif.
> ```css
> .container {
>     display: grid;
>     justify-content: repeat(3, 1fr); /* Repeat 3 times */
>     /* Or use justify-content: repeat(100%, 1fr); and use @media to further apply the content repeat(3, 1fr); */
>     grid-gap: 10px;
> }
> ```
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
* **Menerapkan CSS Link ke Tailwind CSS dan `global.css`.**
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Project{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/global.css' %}">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
```css
/* static/css/global.css */
.context {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100%, 1fr));
    gap: 20px;
    padding: 15px;
    margin: 0 auto;
    width: 100%;
    max-width: 1920px;
    background-color: #b3cde0; /* Apply light indigo background */
    background: linear-gradient(90deg, rgba(255, 255, 255, 0.1) 25%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.1) 75%);
    background-size: 200px 100%;
    animation: shine 2s infinite linear; /* Apply shine animation */
}

@media (min-width: 640px) {
    .context {
        grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); /* Adjust for larger screens */
    }
}

.bg-light-indigo {
    background-color: #b3cde0;
}

.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}

.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #674ea7;
    box-shadow: 0 0 0 3px #674ea7;
}

@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
...
```

* **Membuat `book_cards.html`, `edit_books.html`, `footer.html`, dan beserta logiikanya di `views.py** 
> * **Catatan:** Tailwind css diklasifikasikan di tiap container div / nav / dll dengan `class="actual-class tailwind1 tailwind2 tailwind3 ...`
```html
<!-- book_cards.html -->
<div class="book-cards bg-light-indigo border border-gray-300 rounded-lg shadow-md p-4 flex flex-col items-center justify-start animate-shine">
    <div class="book-image max-w-xs h-auto rounded-lg flex justify-center items-center">
        <img src="{{ book.image.url }}" alt="{{ book.name }}">
    </div>
    <h2 class="font-bold text-lg mt-4">{{ book.name }}</h2>
    <p class="text-justify mt-2">{{ book.description|slice:":150" }}...</p>
</div>
```
```html
<!-- edit_books.html -->
{% extends 'base.html' %}
{% block content %}
<div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Edit Book</h1>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">Save</button>
    </form>
</div>
{% endblock %}
```
```html
<!-- footer.html -->
{% extends 'base.html' %}
{% block content %}
<div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Edit Book</h1>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">Save</button>
    </form>
</div>
{% endblock %}
```
```python
# Edit Book method (to edit_book.html)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('main:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_books.html', {'form': form})
```

## TM6 Questions
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
> * **Asynchronous Processing**: JavaScript mendukung operasi asinkron melalui AJAX, memungkinkan pengambilan data dari server tanpa mengganggu pengalaman pengguna.
> * **Responsibilitas**: Dengan menggunakan asynchronous processing, JavaScript dapat menggunakan berbagai tools seperti fetch API dan AJAX untuk menampilkan respons real-time dari pengguna tanpa perlu refresh atau redirect menuju situs yang lainnya.
> * **Kompatibilitas**: JavaScript secara native berjalan hampir di seluruh browser, baik website umum maupun website secara mobile.
> * **Pengalaman Interaksi**: JavaScript memungkinkan pengembang untuk membuat halaman web yang interaktif, seperti validasi form, animasi, dan manipulasi DOM.
> * **Ekosistem dan Komunitas**: JavaScript menyediakan banyak libraries dan frameworks seperti `React.js`, `Angular`, `Vue`, dan yang lainnya yang mana merupakan pengembangan dari komunitasnya yang sudah besar.

2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi **jika kita tidak menggunakan `await`**?
> * **`await` digunakan untuk menunggu hasil dari operasi asinkron** seperti `fetch()`. Fungsi `fetch()` mengembalikan sebuah *Promise* yang mewakili operasi jaringan yang sedang berlangsung. Dengan menggunakan `await`, kita dapat menunggu hingga *Promise* tersebut selesai dan mengembalikan hasilnya sebelum melanjutkan eksekusi kode berikutnya.
> * **Jika kita tidak menggunakan `await`, maka `fetch()` akan mengembalikan `Promise` yang belum selesai**, dan kita **tidak dapat langsung menggunakan hasil dari operasi jaringan tersebut**. Ini dapat menyebabkan kesalahan atau perilaku yang tidak diinginkan karena data yang diharapkan belum tersedia.

3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk **AJAX POST**?
> * Decorator `csrf_exempt` digunakan untuk **menonaktifkan perlindungan CSRF (Cross-Site Request Forgery)** pada view tertentu. Dekorator ini diperlukan ketika kita melakukan **AJAX POST** karena **permintaan AJAX tidak selalu menyertakan token CSRF secara otomatis**. **Tanpa menonaktifkan perlindungan CSRF, server akan menolak permintaan POST** yang tidak menyertakan token CSRF yang valid.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
> * **Keamanan**: Manipulasi kode seperti XSS injection dapat dilakukan dengan memasukkan kode perusak, seperti kode HTML, CSS, JavaScript, dll untuk merusak atau bahkan mencuri data penting website. **Validasi dengan Frontend saja tidak cukup** karena manipulasinya dapat dilewatkan begitu saja. Oleh karena itu, validasi Backend seperti **CSRF** dan **AJAX** dibutuhkan.
> * **Konsistensi:** Backend bertanggung jawab untuk menyimpan dan memproses data, sehingga validasi di backend memastikan bahwa data yang masuk selalu dalam format yang benar.
> * **Sentralisasi**: Validasi di backend memastikan bahwa semua data yang masuk melalui berbagai jalur (misalnya, API, form, dll.) divalidasi dengan cara yang konsisten.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
* Menge-link JavaScript script berupa file, yakni `global.js` dari `base.html`.
> **`templates/base.html`**
```html
<body>
    {% block content %} {% endblock content %}
    <script type="text/JavaScript" src="{% static 'js/global.js' %}"></script>
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script> <!-- DOMPurify script, dijelaskan di bagian akhir penjelasan -->
</body>
```
* Menambahkan method di `views.py` untuk menambahkan buku dengan **AJAX**, nantinya dengan `fetch()` API. Ubah objek buku agar terfilter per user yang terlogin.
> **`main/views.py`**
```python
...
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
...

@csrf_exempt
@require_POST
def add_book_entry_ajax_form(request):
    if not request.user.is_authenticated:
        return HttpResponse(b"UNAUTHORIZED", status=401)
    
    user = request.user
    name = strip_tags(request.POST.get('name'))
    ...

    # Validasi untuk form yang invalid (termasuk juga XSS injection)
    if name == "" or category == "" or price == 0 or description == ""\
        or quantity == 0 or isbn_13 == "" or isbn_10 == "" \
        or published_date == "" or pages == 0 or language == "" or weight == 0\
        or publisher == "" or author == "":
        return HttpResponse(b"MISSING FIELDS", status=400)

    # Validasi gambar
    if image:
        if not image.content_type.startswith('image/'):
            return HttpResponse(b"INVALID FILE TYPE", status=400)

    new_book = BookEntry(user=user, name=name, category=category, price=price, \
                         description=description, quantity=quantity, \
                         isbn_13=isbn_13, isbn_10=isbn_10, \
                         published_date=published_date, pages=pages, \
                         language=language, weight=weight, \
                         publisher=publisher, author=author, image=image)
    new_book.save()

    return HttpResponse(b"CREATED", 201)

def show_json(request):
    books = BookEntry.objects.filter(user=request.user)
    ...

def show_xml(request):
    books = BookEntry.objects.filter(user=request.user)
    ...
```
* Menggunakan `fetch()` API untuk menampilkan cards buku yang akan ditampilkan. Dengan itu ada perubahan yang dilakukan di `main/templates/main.html`: menambahkan suatu container dengan id `book-cards`, `global.js`, `main/templates/book_cards.html`: penggunaan file ini dibuat untuk mengeliminasi redundansi dan memudahkan validasi, dan `urls.py`: untuk penggunaan file `book_cards.html`. Terdapat beberapa perbedaan dengan tutorial yang dilakukan, seperti yang disebutkan di bawah ini:
> **`main/urls.py`**
```python
from main.views import ... , add_book_entry_ajax_form, ... , book_list
...

urlpatterns = [
    ...
    path('add-book-ajax', add_book_entry_ajax_form, name='add_book_ajax'),
    ...
    path('book-list/', book_list, name='book_list'),
    ...
]
```
> **`static/js/global.js`**
```JavaScript
async function fetchBookCardTemplate() {
    const response = await fetch('/book-list'); // Tujuan book_cards.html
    return await response.text();
}

...

async function refreshBookEntries() {
    document.getElementById("book-cards").innerHTML = "";
    document.getElementById("book-cards").className = "";
    const books = await getBooks();
    let bookEntriesHtml = "";
    let classNameString = "";

    if (books.length === 0) {
        ...
    } else {
        classNameString = "context grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 justify-center items-center";
        const bookCardTemplate = await fetchBookCardTemplate();
        books.forEach((book) => {
            let bookHtml = bookCardTemplate
                .replace(/{{ book.image_url }}/g, DOMPurify.sanitize(book.image_url))
                .replace(/{{ book.name }}/g, DOMPurify.sanitize(book.name))
                .replace(/{{ book.price }}/g, DOMPurify.sanitize(book.price))
                .replace(/{{ book.description }}/g, DOMPurify.sanitize(book.description))
                .replace(/{{ book.category }}/g, DOMPurify.sanitize(book.category))
                .replace(/{{ book.author }}/g, DOMPurify.sanitize(book.author))
                .replace(/{{ book.published_date }}/g, DOMPurify.sanitize(book.published_date))
                .replace(/{{ book.isbn_13 }}/g, DOMPurify.sanitize(book.isbn_13))
                .replace(/{{ book.quantity }}/g, DOMPurify.sanitize(book.quantity))
                .replace(/{{ book.rating_star }}/g, DOMPurify.sanitize(book.rating_star))
                .replace(/{{ book.isbn_10 }}/g, DOMPurify.sanitize(book.isbn_10))
                .replace(/{{ book.publisher }}/g, DOMPurify.sanitize(book.publisher))
                .replace(/{{ book.pages }}/g, DOMPurify.sanitize(book.pages))
                .replace(/{{ book.language }}/g, DOMPurify.sanitize(book.language))
                .replace(/{{ book.weight }}/g, DOMPurify.sanitize(book.weight))
                .replace(/{{ book.pk }}/g, DOMPurify.sanitize(book.pk));
            bookEntriesHtml = bookHtml;
        }); // Penggunaan DOMPurify dijelaskan di bagian akhir; .replace(...) untuk replace validasi Django dengan AJAX
    }
}
```
> **`main/templates/book_cards.html`**
```html
{% for book in books %} <!-- Penggunaan for loop untuk membantu validasi dengan const books yang ada di global.js -->
    ...
{% endfor %}
```
> **Catatan: Penggunaan Django syntax, seperti untuk `fetch()` API mungkin tidak bisa dilakukan di eksternal JS.**
* Menambahkan crudModal untuk menambahkan buku dengan AJAX. Hal ini mengikuti tutorial dengan mengubah `fields` yang diperlukan dan *adjusting* *styles* yang diterapkan: **`fields` yang banyak dapat membuat form crudModal tertutup navbar (atau bahkan footer yang saya terapkan).**
> **`main/templates/main.html`**
```html
<div id="book-cards"></div>
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out"> <!-- Penggunaan overflow-y-auto agar tidak dimakan navbar -->
    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-11/12 sm:w-5/6 md:w-3/4 lg:w-2/3 xl:w-1/2 mx-4 sm:mx-0 max-h-full overflow-y-auto">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-gray-900">
            Add New Book Entry
            </h3>
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
            </svg>
            <span class="sr-only">Close modal</span>
            </button>
        </div>
        <!-- Modal body -->
        <div class="px-6 py-4 space-y-6 form-style">
            <form id="bookEntryForm">
                <div class="mb-4">
                    <label for="name" class="block text-sm font-medium text-gray-700">Book Title</label>
                    <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter book title" required>
                </div>
                ...
            </form>
        </div>
        <!-- Modal footer -->
        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitBookEntry" form="bookEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
        </div>
        </div>
    </div>
    ...
    <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-cyan-400 hover:bg-cyan-500 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
        Add Book with AJAX
    </button>
    ...
```
> **`static/js/global.js`**
```JavaScript
unction addBookEntry() {
    const formElement = document.querySelector('#bookEntryForm');

    fetch('/add-book-ajax', {
        method: "POST",
        body: new FormData(formElement),
        }).then(response => refreshBookEntries())
    
    formElement.reset();
    document.querySelector('[data-modal-toggle="crudModal"]').click();

    return false;
}

document.getElementById('bookEntryForm').addEventListener('submit', function(event) {
    event.preventDefault();
    addBookEntry();
});

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalBtn").addEventListener("click", hideModal);
document.getElementById("submitBookEntry").addEventListener("click", hideModal);
```
> **Catatan: Hanya menampilkan function `addBookEntry()` dan berbagai event listener yang mendapat perubahan yang cukup signifikan daripada tutorial.**
* Menambahkan validasi tambahan di forms.py untuk `strip_tags` dan `DOMPurify` (`sanitize`) untuk sanitasi masukan user: buku baru. **Sudah ada implementasi di atas dan penggunaannya juga mengikuti tutorial.**

### Linked Images: TM3
* https://drive.google.com/file/d/11AqnKIrWYsxieNMhu5dRm2mpgZ4GpFqQ/view?usp=sharing, 
* https://drive.google.com/file/d/1AOkX5NTui4nFmU7RpESOFvzGTiwqVRq8/view?usp=sharing, 
* https://drive.google.com/file/d/1o8YNXCkz7onn0F362bkC3zWpsVt3xOKh/view?usp=sharing, 
* https://drive.google.com/file/d/1zLFi5q2OAdktVpvBiphAvAFkHYBM92tx/view?usp=sharing