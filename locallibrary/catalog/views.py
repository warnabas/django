from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all() #filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'book_list.html'  # Specify your own template name/location
    paginate_by = 5

class BookDetailView(generic.DetailView):
    model = Book

class AuthorView(generic.ListView):
    model = Author
    contex_object_name = "author_list"
    queryset = Author.objects.all()
    template_name = 'author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'

def index(request):
    """Функция отображения для домашней страницы сайта."""
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # Метод 'all()' применен по умолчанию.
    num_authors = Author.objects.count()
    # word = ''.lower() написать функцию ищущую все элементы тратата из пятого раздела
    # вот решение, надо потом вылизать просто его queryset = Book.objects.filter(title__icontains='war')[:5] он ищет во всех заголовках слово вар
    # test_views =  Genre.objects.all().count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)