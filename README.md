# Django-Project
Smart Campus Helpdesk API

This project is a backend REST API built using Django and Django REST Framework for managing support tickets in a Smart Campus system.

Students can create tickets for issues such as classroom, hostel, or network problems. Administrators can view, update, and manage those tickets.

Project Objective

The goal of this project is to implement backend concepts such as:

CRUD operations

JWT authentication

Pagination

Filtering

Ordering

Search functionality

Clean API structure

This project uses PostgreSQL as the database.

Tech Stack

Python

Django

Django REST Framework

PostgreSQL

Simple JWT

Features

User login with JWT authentication

Admin login with session authentication

Create ticket

View all tickets

Retrieve single ticket

Update ticket status

Delete ticket

Filter tickets by category and status

Order tickets by priority and created date

Search by title or description

Pagination for ticket listing

Ticket Model

The Ticket model contains the following fields:

id

title

description

category (classroom / hostel / network)

priority (low / medium / high)

status (open / in-progress / closed)

created_at

updated_at
