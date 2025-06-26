# All-in-One OTT Platform

This Django project is an **All-in-One OTT Platform** that allows users to browse and watch content (movies, shows, series, etc.) from multiple OTT providers (stores) in one place. Users can view content from different platforms, see details, and access content at varied prices depending on the type and quality.

---

## Features

- **Unified Content Catalog:** Browse all movies, shows, and series from multiple OTT platforms in one place.
- **Content Types & Pricing:** Each content item has a type (Free, Basic, Standard, Premium, Premium Plus) that determines its price and quality.
- **Store Integration:** Content is linked to different OTT stores (e.g., Netflix, Prime Video, Hotstar).
- **Detail Pages:** Each content item has a detail page with description, image, and type.
- **Search Stores:** Users can search which stores offer a particular content.
- **Admin Panel:** Manage content, stores, reviews, and certificates via Django admin.
- **Tailwind CSS Integration:** Modern, responsive UI using Tailwind CSS.
- **Live Reload:** Uses `django-browser-reload` for instant template and static file updates during development.

---

## Folder Structure

```
chai_aur_django/
│
├── chai_and_django/         # Main Django project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── trial/                   # Main app for content, stores, reviews, certificates
│   ├── models.py            # Models: content, Store, TrialReview, trialcertificate
│   ├── views.py             # Views for listing, detail, and store search
│   ├── forms.py             # Forms for content/store selection
│   ├── admin.py             # Admin customizations
│   ├── urls.py              # App-specific URLs
│   ├── templates/
│   │   ├── all_trial.html
│   │   ├── trial_detail.html
│   │   └── trial_stores.html
│   └── migrations/          # Django migrations
│
├── templates/               # Project-wide templates
│   ├── layout.html          # Base layout (Tailwind, nav, etc.)
│   ├── index.html           # Home page
│   ├── about.html
│   └── contact.html
│
├── static/                  # Static files (CSS, images)
│   └── styles.css
│
├── media/                   # Uploaded images (content images)
│
├── theme/                   # Tailwind CSS integration (django-tailwind)
│   ├── static_src/
│   └── templates/
│
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
└── readme.md                # This file
```

---

## Workflow

1. **Content Management:**  
   - Admins add content (movies, shows, etc.) with name, image, type, description, and assign to stores.
   - Each content has a type (Free, Basic, Standard, Premium, Premium Plus) that determines its price/quality.

2. **Store Management:**  
   - Admins add OTT stores (e.g., Netflix, Prime Video) and link available content.

3. **User Experience:**  
   - Users land on the home page and can browse all available content.
   - Clicking on a content item shows its details, type, and which stores offer it.
   - Users can search for stores offering a specific content.

4. **Reviews & Certificates:**  
   - Users can leave reviews for content.
   - Each content can have a certificate (e.g., for authenticity or licensing).

5. **Styling & Live Reload:**  
   - Tailwind CSS is used for modern, responsive design.
   - `django-browser-reload` enables live reloading during development.

---

## How to Run

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   npm install  # in theme/static_src if using Tailwind
   ```

2. **Apply migrations:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

4. **Run the development server:**
   ```
   python manage.py runserver
   ```

5. **(Optional) Start Tailwind CSS watcher:**
   ```
   python manage.py tailwind start
   ```

6. **Access the app:**
   - Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Tech Stack

- **Backend:** Django 5.x
- **Frontend:** Tailwind CSS, HTML templates
- **Database:** SQLite (default, can be changed)
- **Live Reload:** django-browser-reload

---