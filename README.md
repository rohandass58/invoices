# Invoices Web Application


## Introduction

The Invoices Web Application is a feature-rich invoicing system built on Django and Django Rest Framework. It allows businesses and individuals to manage their invoices efficiently. Users can create, view, edit, and delete invoices and their associated details. The application also provides RESTful APIs for seamless integration with other systems.

## Features

- User-friendly interface for managing invoices.
- Add, edit, and delete invoices with ease.
- Detailed view of invoice information and associated details.
- RESTful APIs for seamless integration with external systems.
- Role-based access control for secure data management.

## Getting Started

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:rohandass58/invoices.git
   
2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
   
4. Move to the project folder:
   ```bash
   cd invoices
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

    Run the Django development server:
    ```bash 
    python manage.py runserver

    Open your web browser and go to http://localhost:8000/ to access the application.
    
## API ENDPOINTS

{
    "invoice": "http://127.0.0.1:8000/invoices/invoice/",
    "invoice_detail": "http://127.0.0.1:8000/invoices/invoice_detail/"
}









