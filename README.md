# DJ Ecomm — Ecommerce App in Django

A simple e-commerce web application built with **Django**, **Python**, **HTML**, and **CSS**.  
This repository contains the Django project (`djecomm`) and the apps that implement product browsing, cart management, checkout, user authentication, and order handling.

**Repository:** `https://github.com/vivek1702/Ecommerce-App-In-Django`  
**Project folder:** `djecomm/`  

---

## Features
- Product listing, detail pages and category browsing  
- Add to cart / update quantities / remove from cart (session or DB based)  
- Checkout flow and order creation (basic payment integration placeholder)  
- User authentication (register / login / profile / order history)  
- Admin interface for managing products, categories and orders  
- Responsive front-end using HTML & CSS (static files & media handling)

---

## Tech stack
- Python 3.x  
- Django (version used in project)  
- HTML, CSS for frontend templates  
- DB: default PostgresSQL (adjust `settings.py` for other DBs)  

---

## Quick start (local)
1. Clone the repo and change directory into the project folder:
```bash
git clone https://github.com/vivek1702/Ecommerce-App-In-Django.git
cd Ecommerce-App-In-Django/djecomm


## Project structure
djecomm/
├─ manage.py
├─ djecomm/            # Django project settings
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ products/           # app: products (example)
│  ├─ models.py        # Product, Category, ...
│  ├─ views.py
│  └─ templates/
├─ cart/               # app: cart (example)
├─ orders/             # app: orders (example)
├─ accounts/           # app: user auth/profile (example)
├─ templates/
└─ static/

