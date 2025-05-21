
from django.db.models import Sum
from django.utils.timezone import now

from finances.models import Transaction


def user_balance(request):
    if request.user.is_authenticated:
        incomes = Transaction.objects.filter(
            user=request.user,
            category__is_income=True
        ).aggregate(total=Sum('amount'))['total'] or 0

        expenses = Transaction.objects.filter(
            user=request.user,
            category__is_income=False
        ).aggregate(total=Sum('amount'))['total'] or 0

        balance = incomes - expenses

        return {
            'total_balance': balance,
            'today': now().date()
        }

    return {
        'total_balance': 0,
        'today': now().date()
    }