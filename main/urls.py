from django.urls import path
from main.views import show_main, add_book_entry_form, show_json, show_xml, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-book', add_book_entry_form, name='add_book'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
]