# Django Employee Information Dashboard

A simple Django-based web app that displays employee information in two formats:
- As a **responsive HTML table**.
- As **stylized employee cards**.

## 🔧 Technologies Used
- Django (Python)
- HTML & CSS (with basic styling)
- Bootstrap (optional)
- VS Code (for development)

---

## 📂 Project Structure

```
├── create_table/-------------appname
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py        # Contains views: table() and cards()
│   ├── urls.py         # App-level URL routes
│   └── templates/
│         
│       ├── index.html  # Table View
│       └── cards.html  # Card View
├── table/.........projectname
│   ├── settings.py
│   ├── urls.py
│   └── ...
|__________templates/
|```           |
               |_____base.html
               |
               |
               |______nav.html

---

## ▶️ How It Works

### 1. `views.py`
```python
from django.shortcuts import render

def table(request):
  employee = [
      {'Ename':'Anjani',
       'EMPId':1234,
       'Phone_no':9875632571,
       'Role':'Python Developer',
       'Location':'Hyderabad',
       'Salary':700000,
       'DeptNo':'D1',
       'Hiredate':'21-AUG-2025',
       'MGRID':'M1',
       'Shift':'General',
       'PersonalMailId':'srianjani@gmail.com',
       'Gender':'Female',
       'OfficialMailId':'srianjani@office.in',
       'Experience':'6 Months'},
      # ... additional employee records ...
  ]
  ......100 employess data......
  context = { 'data': employee }
  return render(request, 'index.html', context)

def cards(request):
  return render(request, 'cards.html')
```

---

### 2. `index.html` - Table View
```html
{% extends 'base.html' %}
{% block content %}
<table border="2px solid red" style="width: 100%;">
  <tr>
    <th>Ename</th> <th>EMPId</th> <th>Phone_no</th> <th>Role</th> <th>Location</th>
    <th>Salary</th> <th>DeptNo</th> <th>Hiredate</th> <th>MGRID</th> <th>Shift</th>
    <th>PersonalMailId</th> <th>Gender</th> <th>OfficialMailId</th> <th>Experience</th>
  </tr>
  {% for i in data %}
  <tr>
    <td>{{i.Ename}}</td> <td>{{i.EMPId}}</td> <td>{{i.Phone_no}}</td> <td>{{i.Role}}</td>
    <td>{{i.Location}}</td> <td>{{i.Salary}}</td> <td>{{i.DeptNo}}</td> <td>{{i.Hiredate}}</td>
    <td>{{i.MGRID}}</td> <td>{{i.Shift}}</td> <td>{{i.PersonalMailId}}</td>
    <td>{{i.Gender}}</td> <td>{{i.OfficialMailId}}</td> <td>{{i.Experience}}</td>
  </tr>
  {% endfor %}
</table>
{% endblock content %}
```

---

### 3. `cards.html` - Card View
```html
{% extends 'base.html' %}
{% block content %}
<main>
  <div class="card-container">
    <div class="card">
      <div class="card-header python">Python Dev</div>
      <div class="card-content">
        <h3>Anjani</h3>
        <p>EMP ID: 1234</p>
        <p>Hyderabad</p>
        <p>Phone: 9875632571</p>
        <p>Dept No: D1</p>
        <p>Hire Date: 21-AUG-2025</p>
        <p>Shift: General</p>
        <p>Gender: Female</p>
        <p>Experience: 6 Months</p>
        <p>Salary: ₹700,000</p>
        <p>Mail: srianjani@gmail.com</p>
        <span class="tag">Python</span>
      </div>
    </div>
    <!-- More cards follow... -->
  </div>
</main>
{% endblock %}
```

---

### 4. `base.html` - Template Inheritance
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Employee Dashboard</title>
  <style>
    /* Custom CSS for cards and table layout */
    body { font-family: 'Segoe UI', sans-serif; background: #dde4ea; margin: 0; }
    .card-container { display: flex; flex-wrap: wrap; gap: 30px; justify-content: center; }
    .card { width: 220px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    nav { background-color: lightgreen; height: 80px; padding: 0 40%; }
    ol { display: flex; justify-content: space-between; padding-top: 7.5%; list-style: none; }
  </style>
</head>
<body>
  {% include 'nav.html' %}
  {% block content %}
  {% endblock content %}
</body>
</html>
```

---

### 5. `nav.html` - Navigation Bar
```html
<nav>
  <ol>
    <li><a href="{% url 'table' %}">Table_Data</a></li>
    <li><a href="{% url 'cards' %}">Card_Data</a></li>

  </ol>
</nav>
```

---

## ✅ Setup Instructions

1. creating version controll (VS CODE):
python -m venv name of the versioncontrol stystem (ex..version)
   
2. pip list: to check tools


3. activating the version control:
 name of the versioncontrol stystem\scripts\activate

example....

 version\scripts\activate



4. django installation:
pip intsall django



5. creating project:
django-admin startproject projectname

after creating project:
cd projectname

6. code .

7. in vs code cmd:
py manage.py startapp appname


8. For output :
py manage.py runserver 


9. Access the app at `http://127.0.0.1:8000/`





