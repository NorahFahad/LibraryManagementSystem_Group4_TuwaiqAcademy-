from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import (Languages, Authors,
                     Publishers, Categories, Sections,
                     Faculties, Books, eBooks, Copies, News)


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['ID', 'category', 'category_persian']


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['ID', 'category_id', 'section',' section_persian']


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ['ID', 'faculty', 'faculty_persian']


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['ID', 'signatory', 'title',
                  'isbn','pages','language_id',
                  'edition','author_id','publisher_id',
                  'publication_year','section_id','faculty_id',
                  'description']


class eBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = eBooks
        fields = ['ID', 'book_id', 'extension']


class CopiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copies
        fields = ['ID', 'book_id', 'status']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['ID', 'news_title',
                  'news_summary', 'news_details',
                  'news_ref', 'news_title_persian', 'news_details_persian',
                  'news_ref_persian', 'news_date', 'fileext', 'faculties_id']

