from django.test import TestCase, Client
from main.models import BookEntry
from django.utils import timezone
from django.urls import reverse

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_add_book_url_is_exist(self):
        response = Client().get('/add-book')
        self.assertEqual(response.status_code, 200)
    
    def test_add_book_using_add_book_template(self):
        response = Client().get('/add-book')
        self.assertTemplateUsed(response, 'add_book.html')

    def test_show_json_url_is_exist(self):
        response = Client().get('/json/')
        self.assertEqual(response.status_code, 200)

    def test_show_xml_url_is_exist(self):
        response = Client().get('/xml/')
        self.assertEqual(response.status_code, 200)

    # Test for show_json_by_id and show_xml_by_id
    # NOTE: Using the UUID str from Life: My Story Through History
    def test_show_json_by_id_url_is_exist(self):
        response = Client().get('/json/29b77dee-c575-4f6f-bf14-6362cff3bbb5')
        self.assertEqual(response.status_code, 200)

    def test_show_xml_by_id_url_is_exist(self):
        response = Client().get('/xml/29b77dee-c575-4f6f-bf14-6362cff3bbb5')
        self.assertEqual(response.status_code, 200)

    # Error code test for adding book: Rent-A-(Really Shy!)-Girlfriend 3
    def test_add_book(self):
        response = Client().post('/add-book', {
            'name': 'Rent-A-(Really Shy!)-Girlfriend 3',
            'price': 150000,
            'description': "\
                            The official spinoff manga of Rent-A-Girlfriend, the rom-com turned hit anime, features fan-favorite Sumi, the shy girl longing to come out of her shell. Written and illustrated by original creator Reiji Miyajima! Catch up on the manga before Rent-A-Girlfriend returns for a second anime season, coming soon!\n\n\
                            AN UNEXPECTED CLIENT\n\n\
                            Spurred by Mizuhara and determined to make her dream come true, Sumi takes on another date...only to discover that her client is a child! And it’s not only her work life that’s getting hectic. Trips to the nail salon, movie theater, and ramen shop might seem ordinary to most people, but for a girl with poor communication skills, they’re veritable adventures!",
            'quantity': 1,
            'category': 'Light Novel / Manga',
            'isbn_13': '9781646514106',
            'isbn_10': '1646514106',
            'published_date': '2022-11-15',
            'pages': 144,
            'language': 'English',
            'weight': 0.18,
            'author': 'Reiji Miyajima',
            'publisher': 'Kodansha Comics',
            'image': '',
        })

        self.assertEqual(response.status_code, 302)