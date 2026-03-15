```markdown
# Django Portfolio – Web Scraping & Automation Engineer

A modern portfolio website built with **Django** to showcase web scraping projects, technical blogs, and automation solutions.

The website includes project case studies, blog tutorials, and a contact system for potential clients.

---

## Features

- Modern responsive portfolio design
- Projects showcase with images and tags
- Blog system for scraping tutorials
- Blog image gallery support
- Contact form with email notifications
- Skills section with animated progress bars
- Dashboard analytics page
- Footer with Upwork, Fiverr, GitHub, and LinkedIn links
- SEO-friendly blog pages
- Clean UI using TailwindCSS

---

## Tech Stack

Backend
- Django
- Python

Frontend
- TailwindCSS
- HTML
- JavaScript

Database
- SQLite (default)
- Can be upgraded to PostgreSQL for production

Other Tools
- FontAwesome icons
- Markdown blog rendering

---

## Project Structure

```

portfolio/
│
├── core/               # Home page, contact page
├── projects/           # Portfolio projects
├── blog/               # Blog posts and gallery
├── skills/             # Skills section
│
├── templates/          # HTML templates
│
├── static/             # CSS, JS, images
├── media/              # Uploaded files
│
├── manage.py
└── db.sqlite3

```

---

## Installation

### 1. Clone the repository

```

git clone [https://github.com/yourusername/portfolio.git](https://github.com/yourusername/portfolio.git)

```

### 2. Navigate to the project

```

cd portfolio

```

### 3. Create a virtual environment

```

python -m venv venv

```

Activate it:

Mac/Linux

```

source venv/bin/activate

```

Windows

```

venv\Scripts\activate

```

---

### 4. Install dependencies

```

pip install -r requirements.txt

```

---

### 5. Run migrations

```

python manage.py migrate

```

---

### 6. Create superuser

```

python manage.py createsuperuser

```

---

### 7. Run development server

```

python manage.py runserver

```

Open:

```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```

---

## Admin Dashboard

Access the admin panel:

```

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

```

From here you can:

- Add projects
- Add blog posts
- Upload blog gallery images
- Manage skills
- View contact messages

---

## Projects Section

Each project can include:

- Project image
- Gallery images
- Description
- Tech stack
- Tags
- GitHub link
- Live demo link
- Metrics (speed, uptime, records scraped)

---

## Blog System

The blog system supports:

- Markdown content
- Image galleries
- Tags
- Tutorial-style formatting

Used for writing scraping tutorials such as:

- Scrapy guides
- Selenium automation
- BeautifulSoup parsing
- Anti-bot bypass techniques

---

## Deployment

The project can be deployed on:

- Render
- PythonAnywhere
- DigitalOcean
- VPS

Recommended production stack:

```

Django
PostgreSQL
Gunicorn
Nginx

```

---

## Customization

You can easily modify:

- Theme colors
- Footer links
- Social icons
- Projects layout
- Blog styles

Most templates are located in:

```

templates/

```

---

## Author

Farhan Naseer  
Web Scraping & Automation Engineer

Specializing in:

- Web scraping
- Data extraction
- Automation systems
- Anti-bot bypass solutions
- Analytics dashboards

Platforms:

- Upwork
- Fiverr
- GitHub
- LinkedIn

---

## License

This project is open-source and available for educational and portfolio use.

```