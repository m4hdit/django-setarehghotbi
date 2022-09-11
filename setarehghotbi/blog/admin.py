from django.contrib import admin
from .models import (
	BlogModel ,
	TicketModel ,
	SubscribtionEmail ,
	CategoryModels ,
	Comment
	) 


# Register your models here.

admin.site.register(BlogModel)
admin.site.register(TicketModel)
admin.site.register(SubscribtionEmail)
admin.site.register(CategoryModels)
admin.site.register(Comment)