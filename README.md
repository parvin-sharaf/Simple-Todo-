# Simple To-Do App

A simple To-Do application built using the Frappe Framework. This app allows users to create, view, and manage tasks with titles, descriptions, completion status, and due dates. It includes a bonus public web page to display tasks.

---

## Overview

- **App Name**: `simple_todo`
- **Framework**: Frappe (latest stable version)
- **Features**:
  - Create and view tasks.
  - Mark tasks as completed.
  - Auto-hide completed tasks in the list view.
  - Public web page to display all tasks (`/todo`).
- **Developed By**: [Your Name]
- **Contact**: your.email@example.com
- **License**: MIT

---

## Prerequisites

- **Operating System**: Linux (Ubuntu recommended), macOS, or WSL2 with Ubuntu on Windows.
- **Dependencies**:
  - Python 3.10+
  - MariaDB 10.6.6+
  - Node.js 18+
  - Yarn
  - Redis 6
  - wkhtmltopdf 0.12.5+
  - cron

### Install dependencies on Ubuntu:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3.10 python3.10-dev python3-pip mariadb-server nodejs npm redis-server wkhtmltopdf cron
npm install -g yarn
sudo mysql_secure_installation
````

---

## Installation

1. **Install Frappe Bench**:

```bash
pip3 install frappe-bench
bench init frappe-bench
cd frappe-bench
```

2. **Start the Bench Server**:

```bash
bench start
```

3. **Create a New Site**:

```bash
bench new-site todo.localhost
```

Add `127.0.0.1 todo.localhost` to `/etc/hosts`:

```bash
sudo sh -c "echo '127.0.0.1 todo.localhost' >> /etc/hosts"
```

4. **Install the App**:

```bash

bench new-app simple_todo
bench --site todo.localhost install-app simple_todo
```

5. **Migrate the Site**:

```bash
bench --site todo.localhost migrate
```

6. **Access the Site**:

Open your browser and go to: [http://todo.localhost:8000](http://todo.localhost:8000)

---

## Usage

* **Create a Task**:

Go to **Desk → Simple Todo → Task → New**
Fill in `Title`, `Description`, `Due Date`, and `Is Completed`. Save the task.

* **View Tasks**:

Access the list at **Desk → Simple Todo → Task**.
Completed tasks are auto-hidden via client script.

* **Public Task List**:

Visit: [http://todo.localhost:8000/todo](http://todo.localhost:8000/todo)

---

## Configuration

### Enable Developer Mode (optional)

Edit `frappe-bench/sites/todo.localhost/site_config.json`:

```json
{
  "db_name": "...",
  "developer_mode": 1
}
```

Then run:

```bash
bench --site todo.localhost migrate
```

### Client Script for Auto-Hide

Go to **Desk → Client Script → auto hide task**

Script:

```javascript
frappe.listview_settings['Task'] = {
    onload: function(listview) {
        listview.filter_area.clear();
        listview.filter_area.add('Task', 'is_completed', '=', 0);
        listview.refresh();
    }
};
```

### Web Page Template

* Template file: `templates/pages/to-do-list.html`
* Controller: `www/todo.py`

---

## Troubleshooting

* **Site Not Loading**:
  Make sure `bench start` is running and `todo.localhost` is correctly added to `/etc/hosts`.

* **Tasks Not Displaying**:
  Run:

```bash
bench --site todo.localhost mariadb
```


---

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

