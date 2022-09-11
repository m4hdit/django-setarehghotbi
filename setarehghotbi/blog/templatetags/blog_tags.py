from django import template
from ..models import CategoryModels



# register django teplate tags
register = template.Library()


# my teplate tags

@register.inclusion_tag('blog/template_tags/navbar.html')
def navbar(request):
	categorys = CategoryModels.objects.all()
	return {'categorys':categorys,'request':request}



@register.inclusion_tag('blog/template_tags/pagination.html')
def pagination(page_object,url,search=False):
	return {'page_object':page_object,'search':search,'url':url}
