.. _quick_start:

=======================
Quick Start Guide
=======================

This quick start guide will help you get up and running with the "project-13" project in just a few steps.

1. Clone the Repository
-----------------------

Clone the "project-13" repository using the following command:

   ::

      git clone https://github.com/azer7777/project-13.git

Change into the project directory:

   ::

      cd project-13

2. Create a Virtual Environment
-------------------------------

Create a virtual environment:

   ::

      python -m venv venv

Activate the virtual environment:

   - On Windows:

     ::

        .\venv\Scripts\activate

   - On macOS/Linux:

     ::

        source venv/bin/activate

3. Install Dependencies
-----------------------

Install project dependencies using pip:

   ::

      pip install -r requirements.txt

4. Apply Database Migrations
----------------------------

Apply database migrations:

   ::

      python manage.py migrate

5. Create a Superuser Account
------------------------------

Create a superuser account for accessing the Django admin:

   ::

      python manage.py createsuperuser

Follow the prompts to set up the superuser account.

6. Run the Development Server
------------------------------

Start the development server:

   ::

      python manage.py runserver

Open your web browser and navigate to http://127.0.0.1:8000/ to view the application.

That's it! You've completed the quick start guide and can now explore the "project-13" project. For more detailed information, refer to the full :ref:`installation` guide.
