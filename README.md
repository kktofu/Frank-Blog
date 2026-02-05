# Blog System
A personal Blog system built with Django, focusing on backend architecture, data modeling, and maintainable request flow design.
This project allows users to register, log in, create blog posts, and leave comments, with proper authentication and permission control.

![image](https://github.com/kktofu/Frank-Blog/blob/main/blog.jpg)
---

## Features
- User registration and authentication (Django Auth)
- Blog post CRUD (Create, Read, Update, Delete)
- Comment system for logged-in users
- Form validation and input sanitization using Django Forms
- Relational data modeling with Django ORM
- Permission control to prevent unauthorized operations

---

## Tech Stack

- **Backend:** Python, Django  
- **Database:** PostgreSQL  
- **ORM:** Django ORM  
- **Authentication:** Django Auth  
- **Form Handling:** Django Forms

---

## System Architecture Overview

The project follows Django’s MTV (Model–Template–View) pattern:

- **Models:**  
  Define core data structures such as `BlogPost`, `Comment`, and `User`, with clear relationships and responsibilities.

- **Forms:**  
  Centralize validation and data cleaning logic to avoid duplicated validation code in views.

- **Views:**  
  Handle request flow, authentication checks, permission control, and response rendering.

This separation improves readability, maintainability, and future extensibility.

---

## What I Learned

- How Django Forms improve validation consistency and code organization
- Designing relational data models with clear responsibilities
- Implementing authentication and permission control in a real-world web application
- Writing backend code with maintainability in mind, not just functionality

---

## Future Improvements

- Add role-based permissions (e.g., admin / editor)
- Implement pagination for posts and comments
- Add unit tests for forms and views
- Deploy with Docker and CI/CD pipeline

---

## Author

Liu, Hsiu-Fu  
Backend / Full-Stack Engineer
