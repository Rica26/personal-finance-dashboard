from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
# Create your views here.

#ViewSets
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.select_related('category')
    serializer_class = TransactionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#APIViews

class IncomeAPIView(APIView):
    def get(self, request):
        qs = Transaction.objects.filter(category__type='income').annotate(month=ExtractMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
        return Response(qs)
class IncomeYearlyAPIView(APIView):
    def get(self,request, year):
        qs = Transaction.objects.filter(date__year=year, category__type='income').values(month=ExtractMonth('date')).annotate(total=Sum('amount')).order_by('month')
        return Response(qs)

class IncomeYearlyTotalAPIView(APIView):
    def get(self, request, year):
        total = Transaction.objects.filter(date__year=year, category__type='income').aggregate(total=Sum('amount'))['total'] or 0
        return Response({'year': year, 'total': total})
    
class IncomeYearlyCategoryAPIView(APIView):
    def get(self, request, year):
        qs = Transaction.objects.filter(date__year=year, category__type='income').values('category__name').annotate(total=Sum('amount')).order_by('category__name')
        return Response(qs)
    
class IncomeYearlyMonthlyCategoryAPIView(APIView):
    def get(self, request, year):
        qs = Transaction.objects.filter(date__year=year, category__type='income').values('category__name', month=ExtractMonth('date')).annotate(total=Sum('amount')).order_by('month', 'category__name')
        return Response(qs)

class IncomeMonthlyAPIView(APIView):
    def get (self, request, year, month):
        total = Transaction.objects.filter(date__year=year, date__month=month, category__type='income').aggregate(total=Sum('amount'))['total'] or 0
        return Response({'year': year, 'month': month, 'total': total})
    
class IncomeMonthlyCategoryAPIView(APIView):
    def get(self, request, year, month):
        qs = Transaction.objects.filter(date__year=year, date__month=month, category__type='income').values('category__name').annotate(total=Sum('amount')).order_by('category__name')
        return Response(qs)

class ExpenseAPIView(APIView):
    def get(self, request):
        qs = Transaction.objects.filter(category__type='expense').annotate(month=ExtractMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
        return Response(qs)

class ExpenseYearlyAPIView(APIView):
    def get(self, request, year):
        qs = Transaction.objects.filter(date__year=year, category__type='expense').values(month=ExtractMonth('date')).annotate(total=Sum('amount')).order_by('month')
        return Response(qs)

class ExpenseYearlyTotalAPIView(APIView):
    def get(self, request, year):
        total = Transaction.objects.filter(date__year=year, category__type='expense').aggregate(total=Sum('amount'))['total'] or 0
        return Response({'year': year, 'total': total})

class ExpenseYearlyCategoryAPIView(APIView):
    def get(self, request, year):
        qs = Transaction.objects.filter(date__year=year, category__type='expense').values('category__name').annotate(total=Sum('amount')).order_by('category__name')
        return Response(qs)

class ExpenseYearlyMonthlyCategoryAPIView(APIView):
    def get(self, request, year):
        qs = Transaction.objects.filter(date__year=year, category__type='expense').values('category__name', month=ExtractMonth('date')).annotate(total=Sum('amount')).order_by('month', 'category__name')
        return Response(qs)

class ExpenseMonthlyAPIView(APIView):
    def get (self, request, year, month):
        total = Transaction.objects.filter(date__year=year, date__month=month, category__type='expense').aggregate(total=Sum('amount'))['total'] or 0
        return Response({'year': year, 'month': month, 'total': total})

class ExpenseMonthlyCategoryAPIView(APIView):
    def get(self, request, year, month):
        qs = Transaction.objects.filter(date__year=year, date__month=month, category__type='expense').values('category__name').annotate(total=Sum('amount')).order_by('category__name')
        return Response(qs)
