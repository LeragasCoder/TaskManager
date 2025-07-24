# Task Management Django Application

A simple and elegant task management application built with Django that supports creating, editing, and deleting tasks with priority levels and deadlines.

## Features

✅ **CRUD Operations**: Create, Read, Update, and Delete tasks  
🎯 **Priority System**: 4 priority levels (Low, Medium, High, Critical)  
⏰ **Deadline Management**: Set deadlines in days with countdown display  
📊 **Smart Sorting**: Automatic sorting by deadline, priority, and creation date  
🌐 **Persian Text Support**: Automatic RTL direction for Persian text in titles and descriptions  
🎨 **Modern UI**: Beautiful, responsive design with Bootstrap 5 and Dark/Light theme toggle  
👆 **Click-to-Expand**: Click task titles to view descriptions  
🔢 **Status Indicators**: Visual priority badges and urgent task highlighting  

## Requirements

- Python 3.8+
- Django 5.2.4
- Bootstrap 5.3.0 (loaded via CDN)
- Font Awesome 6.0.0 (loaded via CDN)

## Installation & Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd /path/to/ToDoList_Django
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and go to: `http://127.0.0.1:8000/`

## Usage

### Main Features

- **View Tasks**: The main page displays all tasks sorted by urgency
- **Add New Task**: Click "Add New Task" to create a new task
- **Edit Task**: Click the edit icon (✏️) next to any task
- **Delete Task**: Click the delete icon (🗑️) and confirm deletion
- **View Details**: Click on any task title to expand and view its description
- **Auto Direction**: Persian text automatically displays right-to-left in titles and descriptions
- **Theme Toggle**: Switch between dark and light themes with the theme button

### Task Properties

- **Title**: Required, up to 200 characters
- **Description**: Optional, supports multi-line text with automatic Persian/English direction detection
- **Priority**: 4 levels with color coding:
  - 🟢 Low (Green)
  - 🔵 Medium (Blue) 
  - 🟡 High (Orange)
  - 🔴 Critical (Red)
- **Deadline**: Number of days until due date

### Automatic Sorting

Tasks are automatically sorted by:
1. **Deadline** (most urgent first)
2. **Priority** (highest priority first)
3. **Creation date** (oldest first)

## Project Structure

```
ToDoList_Django/
├── todolist_project/          # Main Django project
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   └── ...
├── tasks/                    # Tasks Django app
│   ├── models.py            # Task model definition
│   ├── views.py             # CRUD views
│   ├── forms.py             # Task form
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Django admin configuration
│   └── templates/tasks/     # HTML templates
│       ├── base.html        # Base template with RTL/LTR support
│       ├── task_list.html   # Main task list view
│       ├── task_form.html   # Create/edit task form
│       └── task_confirm_delete.html  # Delete confirmation
├── venv/                    # Virtual environment
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Key Technologies

- **Backend**: Django 5.2.4
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0.0
- **Fonts**: Inter (English), Vazirmatn (Persian)

## Customization

### Adding New Priority Levels
Edit `tasks/models.py` and modify the `PRIORITY_CHOICES` tuple.

### Persian Text Detection
The application automatically detects Persian characters using Unicode range `\u0600-\u06FF` and applies RTL direction to those fields.

### Dark Theme
The application includes a dark theme toggle that:
- Saves theme preference in localStorage
- Provides smooth transitions between themes
- Maintains readability with carefully chosen dark colors
- Works seamlessly with Persian text detection

### Changing Styling
Modify the CSS in `tasks/templates/tasks/base.html` or add custom CSS files.

### Database Configuration
Update `DATABASES` in `todolist_project/settings.py` for production use.

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Admin User
```bash
python manage.py createsuperuser
```

### Access Admin Panel
Visit `http://127.0.0.1:8000/admin/` to manage tasks via Django admin.

## License

This project is created as a demonstration application. Feel free to use and modify as needed.

---

**Happy Task Managing! 🎯** 