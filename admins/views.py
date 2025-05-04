from checkouts.models import Orders
from django.shortcuts import render, get_object_or_404, redirect
import openpyxl
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from io import BytesIO
from checkouts.models import Orders

def orders_list(request):
    orders = Orders.objects.all()
    order_date = request.GET.get('order_date')
    action = request.GET.get('action')
    if order_date:
        orders = orders.filter(created_at__date=parse_date(order_date))
    if action == 'download':
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Orders"
        ws.append(['ID', 'Name', 'Email', 'Phone', 'City', 'Total', 'Paid', 'Status', 'Payment'])
        for order in orders:
            ws.append([
                order.id,
                f"{order.first_name} {order.last_name}",
                order.email,
                order.phone_number,
                order.city,
                float(order.total_amount),
                str(order.paid),
                order.status,
                order.payment_method,
            ])
        output = BytesIO()
        wb.save(output)
        output.seek(0)
        response = HttpResponse(
            output.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename=orders.xlsx'
        return response
    status_choices = Orders.STATUS_CHOICES
    return render(request, 'admins/orders_list.html', {
        'orders': orders,
        'status_choices': status_choices,
    })

def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Orders, id=order_id)
        order.status = request.POST.get('status')
        order.save()
    return redirect('orders_list')