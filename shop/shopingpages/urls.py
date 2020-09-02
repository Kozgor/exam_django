from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('special_offer/', views.special_offer, name="special"),
    path('product_details/<int:product_id>/', views.singleProductDetails, name="singleProduct"),
    path('product_details/', views.product_details, name="product"),
    path('compair/', views.compair, name="productCompair"),
    path('summary/', views.summary, name="productSummary"),
    path('login/', views.login, name="login"),
    path('forgetpass/', views.forgetpass, name="forgetPassword"),
    path('register/', views.register, name="register"),
    path('contact_us/', views.contact, name="contact us"),
    path('normal/', views.normalinfo, name="normalInformation"),
    path('faq/', views.faq, name="faq"),
]