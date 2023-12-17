.. _installation:

=======================
Installation Guide
=======================

This guide will walk you through the process of setting up the "project-13" project on your local machine.

Prerequisites
-------------

Before you begin, ensure that you have the following prerequisites installed on your system:

- Python (>= 3.6)
- pip (Python package installer)

Clone the Repository
--------------------

1. Open a terminal and navigate to the directory where you want to clone the project.

2. Clone the repository using the following command:

   ::

      git clone https://github.com/azer7777/project-13.git

3. Change into the project directory:

   ::

      cd project-13

Create a Virtual Environment
---------------------------

1. Create a virtual environment:

   ::

      python -m venv venv

2. Activate the virtual environment:

   - On Windows:

     ::

        .\venv\Scripts\activate

   - On macOS/Linux:

     ::

        source venv/bin/activate

Install Dependencies
--------------------

1. Install project dependencies using pip:

   ::

      pip install -r requirements.txt

Database Setup
--------------

1. Apply database migrations:

   ::

      python manage.py migrate

2. Create a superuser account (for Django admin access):

   ::

      python manage.py createsuperuser

   Follow the prompts to set up the superuser account.

Run the Development Server
--------------------------

1. Start the development server:

   ::

      python manage.py runserver

2. Open your web browser and navigate to http://127.0.0.1:8000/ to view the application.

That's it! You've successfully installed and set up the "project-13" project on your local machine.
