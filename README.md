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