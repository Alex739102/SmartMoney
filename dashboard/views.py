from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from finances.models import Transaction


@login_required
def dashboard_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    total_income = sum(t.amount for t in transactions if t.category and t.category.is_income)
    total_expense = sum(t.amount for t in transactions if t.category and not t.category.is_income)
    balance = total_income - total_expense

    recent_transactions = transactions[:5]

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'recent_transactions': recent_transactions,
    }

    return render(request, 'dashboard/dashboard.html', context)
