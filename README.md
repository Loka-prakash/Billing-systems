Billing System (Django + MySQL)

• This is a Billing System project that I developed using Django and MySQL.

• The main purpose of this project is to generate customer bills and store them in a database.

• In this system, I can enter product details like price and quantity.

• The system automatically calculates the total amount and adds 12% tax.

• It also shows the currency denomination breakdown for the final amount.

• All the bill details and items are stored in the MySQL database.

• I added a feature to view previous bills anytime.

• The system can generate a PDF invoice using the ReportLab library.

• After creating the bill, it can send the invoice to the customer’s email.

• For email sending, I used Gmail SMTP with an App Password for security.

• I configured the MySQL database and email settings inside settings.py.

• I used virtual environment and installed required packages like django, mysqlclient, and reportlab.

• The project also includes a Django admin panel to manage billing data.

• I can run the project using the command python manage.py runserver.

• Through this project, I learned Django concepts like models, views, templates, database integration, email functionality, tax calculation, and PDF generation.