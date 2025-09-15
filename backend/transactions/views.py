from rest_framework import viewsets
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.select_related('category')
    serializer_class = TransactionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#utils

#serializers

#endpoints


# def filter_by_period(qs, period, year=None, month=None):
#     if period == 'year' and year:
#         qs = qs.filter(date__year=year)
#     elif period == 'month' and year and month:
#         qs = qs.filter(date__year=year, date__month=month)
#     return qs

# def filter_by_category(qs, type=None, category_id=None, name=None):
#     if type and name:
#         if name not in Category.NAME_CHOICES[type]:
#             raise ValueError(f"Categoria '{name}' não pertence ao tipo '{type}'")
        

#     if type:
#         qs = qs.filter(category__type=type)
#     if category_id:
#         qs = qs.filter(category__id=category_id)
#     if name:
#         qs = qs.filter(category__name=name)
#     return qs

# #endpoints

# @api_view(['GET'])
# def income_yearly(request, year):
#     transactions = Transaction.objects.select_related('category').all()
#     transactions = filter_by_period(transactions, 'year', year=year)
#     transactions = filter_by_category(transactions, type='income')
#     total = transactions.aggregate(total=Sum('amount'))['total'] or 0
#     return Response({'year': year, 'income_total': total})

# @api_view(['GET'])
# def income_monthly(request, year, month):
#     transactions = Transaction.objects.select_related('category').all()
#     transactions = filter_by_period(transactions, 'month', year=year, month=month)
#     transactions = filter_by_category(transactions, type='income')
#     total = transactions.aggregate(total=Sum('amount'))['total'] or 0
#     return Response({'year': year, 'month': month, 'income_total': total})

# @api_view(['GET'])
# def expense_yearly(request, year):
#     transactions = Transaction.objects.select_related('category').all()
#     transactions = filter_by_period(transactions, 'year', year=year)
#     transactions = filter_by_category(transactions, type='expense')
#     total = transactions.aggregate(total=Sum('amount'))['total'] or 0
#     return Response({'year': year, 'expense_total': total})

# @api_view(['GET'])
# def expense_monthly(request, year, month):
#     transactions = Transaction.objects.select_related('category').all()
#     transactions = filter_by_period(transactions, 'month', year=year, month=month)
#     transactions = filter_by_category(transactions, type='expense')
#     total = transactions.aggregate(total=Sum('amount'))['total'] or 0
#     return Response({'year': year, 'month': month, 'expense_total': total})


#@api_view(['GET'])
# def summary(request):
#     all_transactions = Transaction.objects.select_related('category').all()
#     def total_by_type(trans_type):
#         return all_transactions.filter(category__type=trans_type).aggregate(total=Sum('amount'))['total'] or 0
#     income_total = total_by_type('income')
#     expense_total = total_by_type('expense')
#     balance = income_total - expense_total

#     def total_by_category(trans_type):
#         qs = all_transactions.filter(category__type=trans_type).values('category__name').annotate(total=Sum('amount'))
#         return {item['category__name']: item['total'] for item in qs}
    
#     income_by_category = total_by_category('income')
#     expense_by_category = total_by_category('expense')

#     def monthly_totals(trans_type):
#         qs = (all_transactions.filter(category__type = trans_type).annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month'))
#         return [{'month': item['month'].strftime('%Y-%m'), 'total': item['total']} for item in qs]

#     income_monthly = monthly_totals('income')
#     expense_monthly = monthly_totals('expense')

#     balance_monthly = {}
#     for item in income_monthly:
#         month = item['month']
#         balance_monthly[month] = balance_monthly.get(month, 0) + item['total']
#     for item in expense_monthly:
#         month = item['month']
#         balance_monthly[month] = balance_monthly.get(month, 0) - item['total']
#     balance_monthly = [{'month': month, 'total': total} for month, total in sorted(balance_monthly.items())]

#     def monthly_category(trans_type):
#         qs = (all_transactions.filter(category__type=trans_type).annotate(month=TruncMonth('date')).values('month', 'category__name').annotate(total=Sum('amount')).order_by('month'))
#         return [{'month': item['month'].strftime('%Y-%m'), 'category': item['category__name'], 'total': item['total']} for item in qs]
#     income_category_monthly = monthly_category('income')
#     expense_category_monthly = monthly_category('expense')

#     balance_category_monthly = {}
#     for item in income_category_monthly:
#         key = (item['month'], item['category'])
#         balance_category_monthly[key] = balance_category_monthly.get(key, 0) + item['total']
#     for item in expense_category_monthly:
#         key = (item['month'], item['category'])
#         balance_category_monthly[key] = balance_category_monthly.get(key, 0) - item['total']
#     balance_category_monthly = [{'month': month, 'category': category, 'total': total} for (month, category), total in sorted(balance_category_monthly.items())]

#     data = {
#     'income_total': income_total,
#     'expense_total': expense_total,
#     'balance': balance,
#     'income_by_category': income_by_category,
#     'expense_by_category': expense_by_category,
#     'income_monthly': income_monthly,
#     'expense_monthly': expense_monthly,
#     'balance_monthly': balance_monthly,
#     'income_category_monthly': income_category_monthly,
#     'expense_category_monthly': expense_category_monthly,
#     'balance_category_monthly': balance_category_monthly,
#     }
    #return Response(data)