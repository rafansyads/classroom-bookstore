from django import forms
from django.forms import ModelForm
from main.models import BookEntry # import the BookEntry model from models.py\
from django.utils.html import strip_tags

class BookEntryForm(ModelForm):
    class Meta:
        model = BookEntry

        fields = [ # list of fields to be included in the form
            'name', 'price', 'description',
            'quantity', 'category', 'isbn_13', 'isbn_10', 'published_date', 
            'pages', 'language', 'weight',
            'author', 'publisher', 'image'
        ] # 'time_added' field is excluded as it is automatically generated
        
        widgets = { # dictionary of widgets to customize the form fields
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        } # customised details: published_date, review_list, image -> widgets 

        labels = { # dictionary of labels to customize the field labels
            'name': 'Book Title',
            'isbn_13': 'ISBN-13',
            'isbn_10': 'ISBN-10',
            'rating_star': 'Rating (0.0 - 5.0)',
        } # labels to be displayed in the form
        
        help_texts = { # dictionary of help texts to provide additional information
            'isbn_13': 'Enter the 13-digit ISBN number.',
            'isbn_10': 'Enter the 10-digit ISBN number.',
            'image': 'Upload an image of the book cover (.jpg, .jpeg, .png).',
        } # help texts to be displayed in the form

    # NOTE: Custom validation methods

    # Custom validation for rating star
    def clean_rating_star(self):
        rating_star = self.cleaned_data.get('rating_star')
        if rating_star is not None and (rating_star < 0.0 or rating_star > 5.0):
            raise forms.ValidationError('Rating must be between 0.0 and 5.0.')
        return rating_star

    # Custom validation for review list
    def clean_review_list(self):
        review_list = self.cleaned_data.get('review_list')
        if not isinstance(review_list, dict):
            raise forms.ValidationError('Review list must be a valid JSON object.')
        return review_list

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description)
    
    def clean_author(self):
        author = self.cleaned_data.get('author')
        return strip_tags(author)
    
    def clean_publisher(self):
        publisher = self.cleaned_data.get('publisher')
        return strip_tags(publisher)
    
    def clean_language(self):
        language = self.cleaned_data.get('language')
        return strip_tags(language)
    
    def clean_category(self):
        category = self.cleaned_data.get('category')
        return strip_tags(category)
    
    def clean_isbn_13(self):
        isbn_13 = self.cleaned_data.get('isbn_13')
        return strip_tags(isbn_13)
    
    def clean_isbn_10(self):
        isbn_10 = self.cleaned_data.get('isbn_10')
        return strip_tags(isbn_10)