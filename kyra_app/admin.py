from django.contrib import admin

# Register your models here.
from kyra_app.models import categories,products,bestsellers
admin.site.register(categories)
admin.site.register(products)
admin.site.register(bestsellers)


