from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
import math
from django.shortcuts import render
from .models import Bill, BillItem



 

import math

TAX_PERCENT = 12


def home(request):
    return render(request, 'index.html')

def calculate_denominations(amount):
    denominations = [500, 200, 100, 50, 20, 10]
    result = {}

    for note in denominations:
        count = amount // note
        if count > 0:
            result[note] = count
            amount = amount % note

    return result



def generate_bill(request):
    if request.method == "POST":
        email = request.POST['email']

        products = []
        total_without_tax = 0

        for i in range(1, 4):
            pid = request.POST.get(f'product{i}_id')
            price = float(request.POST.get(f'product{i}_price', 0))
            qty = int(request.POST.get(f'product{i}_qty', 0))

            purchase = price * qty
            tax = purchase * TAX_PERCENT / 100
            total = purchase + tax

            total_without_tax += purchase

            products.append({
                "pid": pid,
                "price": price,
                "qty": qty,
                "purchase": purchase,
                "tax": tax,
                "total": total
            })

        total_tax = total_without_tax * TAX_PERCENT / 100
        net_price = total_without_tax + total_tax
        rounded_price = math.floor(net_price)

        amount_paid = float(request.POST['amount_paid'])
        balance = amount_paid - rounded_price

        denominations = calculate_denominations(int(balance))

    #    data 

        bill = Bill.objects.create(
            email=email,
            total_amount=rounded_price,
            amount_paid=amount_paid,
            note_500=denominations.get(500, 0),
            note_200=denominations.get(200, 0),
            note_100=denominations.get(100, 0),
            note_50=denominations.get(50, 0),
            note_20=denominations.get(20, 0),
            note_10=denominations.get(10, 0),
            note_5=denominations.get(5, 0),
            note_2=denominations.get(2, 0),
            note_1=denominations.get(1, 0),
        )

        for p in products:
            BillItem.objects.create(
                bill=bill,
                product_id=p["pid"],
                price=p["price"],
                quantity=p["qty"],
                subtotal=p["purchase"]
            )

        # pdf 

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer)
        elements = []

        styles = getSampleStyleSheet()
        elements.append(Paragraph("INVOICE", styles['Title']))
        elements.append(Spacer(1, 0.3 * inch))

        data = [["Product ID", "Price", "Qty", "Purchase", "Tax", "Total"]]

        for p in products:
            data.append([
                p["pid"],
                str(p["price"]),
                str(p["qty"]),
                str(p["purchase"]),
                str(p["tax"]),
                str(p["total"]),
            ])

        data.append(["", "", "", "", "Net Total", str(rounded_price)])

        table = Table(data)
        table.setStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
        ])

        elements.append(table)
        doc.build(elements)

        pdf = buffer.getvalue()
        buffer.close()

        # email 

        email_message = EmailMessage(
            subject="Your Invoice is Here",
            body="Please find attached your invoice.",
            to=[email],
        )

        email_message.attach("invoice.pdf", pdf, "application/pdf")
        email_message.send()

        return render(request, 'bill.html', {
            'email': email,
            'products': products,
            'total_without_tax': total_without_tax,
            'total_tax': total_tax,
            'net_price': net_price,
            'rounded_price': rounded_price,
            'balance': balance,
            'denominations': denominations
        })

    return render(request, 'index.html')



def previous_bills(request):
    bills = Bill.objects.all()
    return render(request, 'previous_bills.html', {'bills': bills})


def bill_detail(request, bill_id):
    bill = Bill.objects.get(id=bill_id)
    items = BillItem.objects.filter(bill=bill)
    return render(request, 'bill_detail.html', {
        'bill': bill,
        'items': items
    })

# Create your views here.
