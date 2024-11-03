from django.http import HttpResponse
from django.shortcuts import render
from main.models import Product
from main.models import Category
from django.shortcuts import get_object_or_404



from django.views.generic import TemplateView, UpdateView , ListView , DetailView



def index(request):
    pass

class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(parent_id__isnull=True)        


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        category = self.get_object()
        subcategories = category.children.all()
        products = category.products.all()
        print(products)

        sort_by = self.request.GET.get('sort', None)
        if sort_by == 'asc':
            products = products.order_by('price')
        elif sort_by == 'desc':
            products = products.order_by('-price')

        breadcrumb = []
        current = category
        while current:
            breadcrumb.append(current)
            current = current.parent
        breadcrumb.reverse()

        context.update({
            'subcategories': subcategories,
            'products': products,
            'breadcrumb': breadcrumb,
        })
        return context

def test(request):
    category = Category.objects.get(id=4)
    print(category.products.all())

    return HttpResponse(f'Product')