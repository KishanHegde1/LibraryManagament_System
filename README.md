# 📚 Library Management System (BiblioHub)

A robust, modern web application designed to handle the core administrative operations of a contemporary library. Built with a powerful **Flask (Python)** backend and styled cleanly using **Tailwind CSS**, this system relies on asynchronous JavaScript `fetch` payloads to execute complete database transactions without requiring full page reloads.

---

## 🛠️ System Features & Capabilities

*   **Asynchronous CRUD Architecture**: Complete **Insert, Update, and Delete** functions communicate via JSON payloads directly over the REST API endpoints.
*   **Comprehensive Schema Coverage**: Directly implements all tables, tracking fields, constraints, and relational data mappings derived from your requirements.
*   **Responsive Control Dashboard**: An intuitive sidebar navigation menu with modal-driven layout components optimized for quick library data entry.

---

## 🗄️ Database Architecture & Relational Schema

The database matches the structural design outlined in the project documentation:

*   **Member**: Handles borrower registration (`member_id`, `name`, `phone`, `membership_date`).
*   **Author**: Keeps track of cataloged writers (`author_id`, `name`).
*   **Book**: Stores individual title instances, subject genres, and live status states (`book_id`, `title`, `author_id`, `category`, `price`, `availability`).
*   **Issue**: Tracks book movement dates between the library and active members (`issue_id`, `member_id`, `book_id`, `issue_date`, `return_date`).
*   **Fine**: Records outstanding penalty balances and monetary transaction statuses (`fine_id`, `member_id`, `amount`, `paid_status`).
*   **Staff**: Logs employee roster data and internal professional assignments (`staff_id`, `name`, `role`).

---

## 🚀 Local Installation & Setup Guide

### 1. Prerequisites
Ensure you have the following installed on your machine:
*   Python 3.x
*   MySQL Server (with Workbench or command-line access)
*   Git

### 2. Set Up the MySQL Database
Log into your local MySQL console and run the database initialization commands found in your documentation:

```sql
CREATE DATABASE library_db;
USE library_db;

-- 1. Run your table creation scripts here...
-- 2. Populate tables using your sample records per entity.
