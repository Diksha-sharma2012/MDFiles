from myapp.models import Product

# Retrieve a specific record
try:
    record = Product.objects.get(id=1)
    # Delete the record
    record.delete()
    print("Record deleted successfully")
except Product.DoesNotExist:
    print("Record not found")
