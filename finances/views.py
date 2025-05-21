from datetime import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm




class CategoryCreateView(LoginRequiredMixin, CreateView):

    model = Category
    form_class = CategoryForm
    template_name = 'finances/category_form.html'
    success_url = '/dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['page_title'] = 'Adaugă o categorie nouă'
        return context


class CategoryListView(LoginRequiredMixin, ListView):

    model = Category
    template_name = 'finances/category_list.html'
    context_object_name = 'categories'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):

    model = Category
    template_name = 'finances/category_delete.html'
    success_url = '/dashboard'


class TransactionCreateView(LoginRequiredMixin, CreateView):

    model = Transaction
    form_class = TransactionForm
    template_name = 'finances/transaction_form.html'
    success_url = '/dashboard'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionListView(LoginRequiredMixin, ListView):

    model = Transaction
    template_name = 'finances/transaction_list.html'
    context_object_name = 'transactions'


class TransactionDetailView(LoginRequiredMixin, DetailView):

    model = Transaction
    template_name = 'finances/transaction_detail.html'
    context_object_name = 'transaction'

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'finances/transaction_update.html'
    success_url ='/transaction_list'

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'finances/transaction_delete.html'
    success_url = '/transaction_list'

