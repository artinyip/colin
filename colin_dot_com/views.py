# Create your views here.

import logging
import datetime

from django.core import serializers
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import loader, RequestContext
from django.shortcuts import render

from colin_dot_com.models import Product, ShortSize, Color, Material, Company, Photo, Project
from colin_dot_com.forms import ProductForm

logger = logging.getLogger("colin")

def index(request):
    return HttpResponseRedirect("/products/")

def list_companies(request):
    companies = Company.objects.order_by("-date_added")[:100]
    template = loader.get_template('colin_dot_com/company_list.html')
    context = {
        'companies' : companies,
    }
    return HttpResponse(template.render(context, request))

def show_company(request, company_id=None):
    logger.debug("user " + request.user.username.__str__())
    if (company_id is not None):
        company = Company.objects.get(pk=company_id)
    else:
        raise Http404("Company not found.")

    template = loader.get_template('colin_dot_com/show_company.html')
    context = RequestContext(request, {
        'company' : company,
    })
    return HttpResponse(template.render(context, request))

def list(request):
    products = Product.objects.order_by('-pub_date')[:100]
    template = loader.get_template('colin_dot_com/list.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

def show(request, product_id=None, product_url=None):
    try:
        if (product_id is not None):
            product = Product.objects.get(pk=product_id)
        elif (product_url is not None):
            product = Product.objects.get(short_url=product_url)
        else:
            raise Http404("Product not found.")
    except:
        raise Http404("Product not found.")
    template = loader.get_template('colin_dot_com/show.html')
    context = RequestContext(request,  {
        'product' : product
    })
    format = request.GET.get('format')
    if (format == 'json'):
        return JsonResponse(serializers.serialize('json', [product]), safe=False)
    return HttpResponse(template.render(context, request))

def add(request):
    if (request.method == 'GET'):
        template = loader.get_template('colin_dot_com/add.html')
        # sizes = ShortSize.objects.all()
        # colors = Color.objects.all()
        # materials = Material.objects.all()
        # context = RequestContext(request, {
        #     'sizes' : sizes,
        #     'colors' : colors,
        #     'materials' : materials
        # })
        form = ProductForm(request.POST)
        return render(request, 'colin_dot_com/add2.html', {'form': form})
    if (request.method == 'POST'):
        logger.debug(request.POST.get("name"))

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()



        # product = Product(
        #     name=request.POST['name'],
        #     description=request.POST['description'],
        #     pub_date=datetime.datetime.now(),
        #     color=Color.objects.get(name=request.POST['color']),
        #     short_size=ShortSize.objects.get(name=request.POST['size']),
        #     material=Material.objects.get(name=request.POST['material']),
        #     price=float(request.POST['price']),
        #     image=request.POST['image'],
        # )
        # for upfile in request.FILES.getlist('image'):
        #     filename = upfile.name
        #     fd = open(filename, 'w+')
        #     for chunk in upfile.chunks:
        #         fd.write(chunk)
        #     fd.close()
        # product.save()
        return HttpResponseRedirect("/products/")
