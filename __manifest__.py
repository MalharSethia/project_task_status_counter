{
    'name': 'Project Task Status Counter',
    'version': '17.0.1.0.0',
    'category': 'Project',
    'summary': 'Display task status counts in project kanban view',
    'description': '''
        This module adds status count badges to project kanban cards showing
        the count of tasks for each status (state) in the project using Odoo's
        existing UI patterns.
    ''',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['project'],
    'data': [
        'views/project_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_task_status_counter/static/src/css/status_counts.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
