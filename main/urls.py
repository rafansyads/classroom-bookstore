from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import show_main, add_book_entry_form, add_book_entry_ajax_form, show_json, show_xml, \
    show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_book, delete_book, book_list, \
    create_book_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-book', add_book_entry_form, name='add_book'),
    path('add-book-ajax', add_book_entry_ajax_form, name='add_book_ajax'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('book-list/', book_list, name='book_list'),
    path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/<uuid:id>', edit_book, name='edit_book'),
    path('delete/<uuid:id>', delete_book, name='delete_book'),
    path('create-flutter/', create_book_flutter, name='create_book_flutter'),
]