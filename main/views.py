from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "index.html"


class HomeView(TemplateView):
    template_name = "views/home.html"


class AboutView(TemplateView):
    template_name = "partials/aboutView.html"


class ProductView(TemplateView):
    template_name = "partials/productView.html"


class VitaminView(TemplateView):
    template_name = "partials/vitaminView.html"


class CategoryView(TemplateView):
    template_name = "partials/categoryView.html"


class PreservativeView(TemplateView):
    template_name = "partials/preservativeView.html"


class BugdialogView(TemplateView):
    template_name = "partials/bugDialog.html"
