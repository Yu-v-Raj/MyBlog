# 📝 MyBlog – Django Blogging Platform

MyBlog is a full-stack blogging platform built using Django.  
It allows users to register, log in, create posts, edit or delete their own posts, comment on posts, search content, and toggle between light and dark themes.

This project demonstrates a strong understanding of Django’s architecture including models, views, templates, authentication system, and secure request handling.

---

## 🚀 Features

### 👤 Authentication System
- User Signup & Login
- Secure Logout (POST-based)
- Password hashing using Django's built-in authentication
- Session-based authentication management

### 📝 Blog Management
- Create new posts
- Edit & delete posts (Author-only permission)
- Slug-based SEO-friendly URLs
- Profile page showing user-specific posts

### 💬 Comment System
- Add comments to posts
- Delete own comments
- One-to-many relationship between Post and Comment

### 🔎 Search Functionality
- Search posts by title
- GET-based query filtering

### 🎨 UI Enhancements
- Clean and responsive layout
- Light / Dark Mode toggle (LocalStorage-based persistence)
- Hover animations and styled blog cards

### 🔐 Security
- CSRF protection on all forms
- Author-based permission checks
- Login-required route protection

---

## 🏗 Project Architecture

### Models
- **Post**
  - Title
  - Slug
  - Content
  - Author (ForeignKey to User)
  - Created timestamp

- **Comment**
  - Post (ForeignKey to Post)
  - Author (ForeignKey to User)
  - Content
  - Created timestamp

### Views
- CRUD operations for Posts
- Comment handling
- Authentication integration
- Search filtering
- Profile-based filtering

### Templates
- Django Template Language (DTL)
- Reusable base layout
- Conditional rendering based on authentication

---

## 🛠 Tech Stack

- Python 3.12
- Django 6
- SQLite (Development)
- HTML5
- CSS3
- JavaScript (Dark Mode Toggle)
- Django Authentication System

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/myblog.git
cd myblog
