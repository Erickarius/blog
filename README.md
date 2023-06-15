# Blog

This is a blog project built with Django framework based on Antonio Mele's book, "Django 3 By Example". The blog utilizes a PostgreSQL database.

## System Requirements

Before running the application, make sure you have the following dependencies installed:

- Python 3.7 or higher
- Django 3.1.0 or higher
- PostgreSQL 10.0 or higher

If you don't have the above dependencies installed, refer to their official documentation for installation instructions on your system.

## Installation

1. Clone this repository to your local machine:

```shell
git clone https://github.com/Erickarius/blog.git
```

2. Navigate to the project directory:

```shell
git clone https://github.com/Erickarius/blog.git
```

3. It is recommended to create and activate a Python virtual environment to maintain a clean environment:

```shell
python3 -m venv venv
source venv/bin/activate
```

4. Install the dependencies using the pip package manager:

```shell
pip install -r requirements.txt
```

5. Perform the database migrations to create the necessary tables:

```shell
python manage.py migrate
```

6. Start the Django development server:

```shell
python manage.py runserver
```

The application should now be accessible at `http://localhost:8000/blog`.

## Features

1. Post Editing with CKEditor: The blog utilizes CKEditor, enabling users to conveniently edit post content.
2. Email Post Sharing: Users can share blog posts by sending them to a chosen email address.
3. Tag-based Post Search: The blog includes a feature to search for posts based on assigned tags, allowing users to easily find content of interest.
4. Post Search: The blog offers a general post search functionality, enabling users to search for content based on entered queries.
5. Post Commenting: Users can add comments to posts, facilitating interaction with authors and other blog readers.
6. Related Post Recommendations: Based on the currently viewed post, the blog also displays suggestions for related posts, keeping users engaged and encouraging further reading.
7. RSS Channel Subscription: Users can subscribe to the blog's RSS channel, receiving notifications about new posts or updates.

## Screenshots

### Main Site:
![blog_main_site](https://github.com/Erickarius/blog/assets/117024079/e64be8c2-c10f-458a-9146-0652cff6f7b6)

### Post Site:
![blog_post_site](https://github.com/Erickarius/blog/assets/117024079/2ae5c107-5675-4d6b-bea6-0e696ab55e69)

### Comments Section:
![blog_comments](https://github.com/Erickarius/blog/assets/117024079/af1a7701-d984-4fd2-813f-26a238f708e8)

### Share Post:
![blog_share](https://github.com/Erickarius/blog/assets/117024079/1a0b2e0c-5bdd-4a55-b8f0-a7d7958711f2)

### Tag Cloud:
![blog_tags](https://github.com/Erickarius/blog/assets/117024079/0cda6e13-e3ca-4b67-acbe-54b0bea1d58b)

### Post Search:
![blog_post_search_1](https://github.com/Erickarius/blog/assets/117024079/6591d33d-31a2-4e7f-b503-3e92eae1eb6c)

![blog_post_search_2](https://github.com/Erickarius/blog/assets/117024079/6f2849ea-177d-4d86-a845-5b1969d97dc7)

### Admin Panel:
![blog_custom_admin_panel](https://github.com/Erickarius/blog/assets/117024079/5abe4cb4-73d3-49d8-86a6-bf404780bc33)
