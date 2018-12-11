from django.conf.urls import url
from . import views
from myshop.views import Tienda
app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', Tienda, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detalleProducto, name='detalleProducto'),
]
