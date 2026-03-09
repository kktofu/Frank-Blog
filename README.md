# Blog System
A personal Blog system built with Django, focusing on backend architecture, RESTful API design, data modeling, and maintainable request flow.
This project allows users to register, log in, create blog posts, and leave comments, with token-based authentication, permission control, and query optimization.

![image](https://github.com/kktofu/Frank-Blog/blob/main/blog.jpg)
---

## Features
- User registration and authentication (Django Auth & JWT)
- RESTful API for BlogPost and Comment (CRUD operations)
- Comment system for logged-in users
- Form validation and input sanitization using Django Forms
- Relational data modeling with Django ORM (User → Post → Comment)
- Object-level permission control to prevent unauthorized operations
- Query optimization using select_related and prefetch_related to avoid N+1 query problems

---

## Tech Stack

- **Backend:** Python, Django, Django REST Framework  
- **Database:** PostgreSQL / SQLite  
- **ORM:** Django ORM  
- **Authentication:** Django Auth, JWT  
- **Form Handling:** Django Forms
- **Testing:** Django TestCase

---

## System Architecture Overview

The project follows Django’s MTV (Model–Template–View) pattern:

- **Models:**  
  Define core data structures such as `BlogPost`, `Comment`, and `User`, with clear relationships and responsibilities.

- **Forms:**  
  Centralize validation and data cleaning to ensure consistency across the app.

- **Views:**  
  Handle request flow, authentication, object-level permissions, and response rendering.
Optimized database queries to prevent N+1 problems with select_related and prefetch_related.

This separation improves readability, maintainability, and future extensibility.

---

## What I Learned

- Building RESTful APIs using Django REST Framework
- Implementing JWT authentication for stateless security
- Using object-level permission control to protect resources
- Optimizing ORM queries with select_related and prefetch_related to avoid N+1 issues
- Writing unit tests for models
- Designing relational data models and maintaining code readability

---

## Future Improvements

- Add role-based permissions (e.g., admin / editor)
- Implement pagination for posts and comments
- Add filtering and search functionality for API endpoints
- Continuous integration with automated tests
- Deploy with Docker and CI/CD pipeline

---

## Author

Liu, Hsiu-Fu  
Backend / Full-Stack Engineer
