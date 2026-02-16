from django.db import models


class Bill(models.Model):
    email = models.EmailField()
    total_amount = models.FloatField(default=0)
    amount_paid = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Denomination fields
    note_500 = models.IntegerField(default=0)
    note_200 = models.IntegerField(default=0)
    note_100 = models.IntegerField(default=0)
    note_50 = models.IntegerField(default=0)
    note_20 = models.IntegerField(default=0)
    note_10 = models.IntegerField(default=0)
    note_5 = models.IntegerField(default=0)
    note_2 = models.IntegerField(default=0)
    note_1 = models.IntegerField(default=0)

    def __str__(self):
        return f"Bill {self.id} - {self.email}"


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    subtotal = models.FloatField()

    def __str__(self):
        return self.product_id

