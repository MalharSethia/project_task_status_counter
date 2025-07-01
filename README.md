# Project Task Status Counter

Odoo module that displays task status count badges on project kanban cards.

## Features

- Shows count badges for each task status on project cards
- Counts ALL tasks (including completed/archived)
- Color-coded badges with tooltips showing percentages

## Installation

1. Copy module to your Odoo addons directory
2. Update Apps List
3. Install "Project Task Status Counter"

## Supported Task States

- `01_in_progress` - Blue badge
- `02_changes_requested` - Orange badge  
- `03_approved` - Teal badge
- `1_done` - Green badge
- `1_canceled` - Red badge

## Requirements

- Odoo 17.0+
- project module

## File Structure

```
project_task_status_counter/
├── __manifest__.py
├── models/project.py
├── views/project_views.xml
└── static/src/css/status_counts.css
```
