from django.shortcuts import render,redirect

def home(Request):
    return render(Request,"index.html")

def about(Request):
    return render(Request,"about.html")

def contact(Request):
    return render(Request,"contact.html")

def product(Request):
    return render(Request,"product.html")

def additionalFeatures(Request):
    return render(Request,"additional-features.html")

def supported(Request):
    return render(Request,"supported.html")

# def qaac(Request):
#     return render(Request,"qaac.html")

# def dal(Request):
#     return render(Request,"dal.html")

# def pmsas(Request):
#     return render(Request,"pmsas.html")

def whyGofresh(Request):
    return render(Request,"why-gofresh.html")