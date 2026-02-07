# 🎬 Movie Reviews

This web application was created as the first practical assignment for the **ST0251** course at **Universidad EAFIT**. It’s a simple, functional movie catalog built with **Django**, showing how to organize data, manage movies, and present them in a clean, responsive interface.

---

## 📝 What It Does
"Movie Reviews" is a place to explore movies stored in a central database. It separates the data, logic, and design so everything works smoothly and is easy to understand.

## 🎨 Design & Interface
The site is made to be friendly and easy to use:

* **Header & Branding**: A bright, eye-catching title with a purple gradient.
* **Background**: Soft blue for a fresh and clean look.
* **Search Bar**: Easy to find and lets you look for movies by title.
* **Movie Cards**: Each movie shows its poster, description, and a "More info" button.
* **Footer**: Dark blue footer with credits and copyright.

## 🚀 Main Features
* **Manage Movies**: Add, edit, and delete movies through Django’s admin panel.
* **Search Movies**: Quickly find movies with a real-time search filter.
* **Upload Posters**: Add images for each movie.
* **Mobile Friendly**: Works on phones, tablets, and desktops.

## 🛠️ Tools Used
* **Framework**: Django (Python)
* **Design**: Bootstrap 5.3 & custom CSS
* **Database**: SQLite
* **Version Control**: Git & GitHub



## 👤 Author / Credits

* **Created by:**  
Isabella Cadavid Posada

* **Course:**  
ST0251 - 2026-1  

* **Institution:**  
Universidad EAFIT


---

## 💻 How to Run It
Follow these steps to see the project on your computer:

### 1. Clone the repository
```bash
git clone https://github.com/IsabellaCada2506/Taller1_P1
cd moviereviewsproject

2. Create a virtual environment
Bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

3. Install Django
Bash
pip install django

4. Set up the database
Bash
python manage.py makemigrations
python manage.py migrate

5. Run the server
Bash
python manage.py runserver

6. Open the site
Go to http://127.0.0.1:8000/ in your browser.

---

