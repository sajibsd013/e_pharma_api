from email.policy import default
from django.db import models
from django.utils.timezone import now
from users.models import MyUser

# Create your models here.

# Create your models here.
STATUS_CHOICES = (
    ('pending', 'pending'),
    ('cancelled', 'cancelled'),
    ('completed', 'completed'),
    ('approved', 'approved'),
)
PAYMENT_CHOICES = (
    ('unpaid', 'unpaid'),
    ('pending', 'pending'),
    ('paid', 'paid'),
)
PAYMENT_METHOD = (
    ('Cash on Delivery', 'Cash on Delivery'),
    ('Bkash', 'Bkash'),
    ('Nogod', 'Nogod'),
    ('Rocket', 'Rocket'),
    ('Upay', 'Upay'),
)




# lets us explicitly set upload path and filename
def upload_to_product(instance, filename):
    return 'images/product/{filename}'.format(filename=filename)



class Product(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.CharField(max_length=120, null=True)
    offer = models.CharField(max_length=120, null=True)
    price = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_to_product)
    description = models.TextField()


    def __str__(self):
        return f"{self.name} - ({self.category})"

    class Meta:
        verbose_name_plural = "Product"
        db_table = "product"

class Order(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    total_cost = models.CharField(max_length=120, null=True, blank=True, default="")
    user_id = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(default=now, editable=False)
    payment_method = models.CharField(
        max_length=120, choices=PAYMENT_METHOD, default="Cash on Delivery", )
    transaction_id = models.CharField(max_length=120, null=True, blank=True, default="")
    payment_status = models.CharField(
        max_length=120, choices=PAYMENT_CHOICES, default="unpaid", )
    service_status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending", )
    products = models.ManyToManyField(Product)
    address = models.TextField()

    class Meta:
        verbose_name_plural = "Order"
        db_table = "Order"



# lets us explicitly set upload path and filename
def upload_to_medicine(instance, filename):
    return 'images/medicine/{filename}'.format(filename=filename)


TYPE_CHOICES = (
    ('Tablet', 'Tablet'),
    ('Capsule', 'Capsule'),
    ('Injection', 'Injection'),
    ('Pediatric Drop', 'Pediatric Drop'),
    ('Suspension', 'Suspension'),
    ('Powder for Suspension', 'Powder for Suspension'),
    ('IV Injection', 'IV Injection'),
    ('Cream', 'Cream'),
    ('Gel', 'Gel'),
    ('Infusion', 'Infusion'),
    ('Nebulizer  Solution', 'Nebulizer  Solution'),
    ('Syrup', 'Syrup'),
    ('Sachet', 'Sachet'),
    ('Eye Drop', 'Eye Drop'),
    ('Eye Oinment', 'Eye Oinment'),
)

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=120)
    weight = models.CharField(max_length=120)
    medicine_type = models.CharField(
        max_length=120, choices=TYPE_CHOICES)
    generic_name = models.CharField(max_length=120,null=True)
    brand_name = models.CharField(max_length=120)
    unit_price = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.medicine_name} - ({self.medicine_type}) - ({self.brand_name})"

    class Meta:
        verbose_name_plural = "medicine"
        db_table = "medicine"
