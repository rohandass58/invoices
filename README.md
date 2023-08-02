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
   git clone https://github.com/your-username/invoices.git
   
2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
   
4. Move to the project folder:
   ```bash
   cd invoices
5. Install the required dependencies:
   ```bash
   pip ibstall -r requirements.txt

## Usage

    Run the Django development server:
    ```bash 
    python manage.py runserver

    Open your web browser and go to http://localhost:8000/ to access the application.

    Create a new invoice by clicking the "Create Invoice" button on the homepage. Fill in the required details and click "Save" to create the invoice.

    View all invoices by going to the homepage, where you will see a list of all the created invoices. Click on an invoice to view its details.

    Add invoice details when viewing an invoice. Click on the "Add Invoice Details" button and fill in the details to add them to the invoice.

    Edit or delete invoices by clicking the "Edit" button to modify the invoice details or the "Delete" button to remove the invoice.

## API Endpoints

The application also provides RESTful APIs for programmatic access to invoices and details. Below are the main API endpoints:

    GET /api/invoices/: Retrieve a list of all invoices.
    POST /api/invoices/: Create a new invoice.
    GET /api/invoices/<invoice_id>/: Retrieve details of a specific invoice.
    PUT /api/invoices/<invoice_id>/: Update details of a specific invoice.
    DELETE /api/invoices/<invoice_id>/: Delete a specific invoice.
    GET /api/invoice_details/: Retrieve a list of all invoice details.
    POST /api/invoice_details/: Create a new invoice detail.
    GET /api/invoice_details/<invoice_detail_id>/: Retrieve details of a specific invoice detail.
    PUT /api/invoice_details/<invoice_detail_id>/: Update details of a specific invoice detail.
    DELETE /api/invoice_details/<invoice_detail_id>/: Delete a specific invoice detail.

For more information on API usage and authentication, please refer to the API documentation.






