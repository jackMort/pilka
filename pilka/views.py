from django.views.generic.base import TemplateView

class Index( TemplateView ):
    template_name = 'index.html'

index = Index.as_view()
