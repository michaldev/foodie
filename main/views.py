from django.views.generic import TemplateView

    
class Homepage(TemplateView):
    template_name = "index.html"    


class ProductView(TemplateView):
    template_name = "partials/productView.html"    