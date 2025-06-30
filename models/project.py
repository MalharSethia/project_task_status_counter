from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    # Individual count fields for each status - easier to work with in templates
    task_in_progress_count = fields.Integer(
        string='In Progress Tasks Count', 
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_changes_requested_count = fields.Integer(
        string='Changes Requested Tasks Count',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_approved_count = fields.Integer(
        string='Approved Tasks Count',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_done_count = fields.Integer(
        string='Done Tasks Count',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_canceled_count = fields.Integer(
        string='Canceled Tasks Count',
        compute='_compute_task_status_counts', 
        store=False
    )
    
    @api.depends('task_ids.state')
    def _compute_task_status_counts(self):
        """Compute the count of tasks for each status"""
        for project in self:
            if not project.task_ids:
                project.task_in_progress_count = 0
                project.task_changes_requested_count = 0
                project.task_approved_count = 0
                project.task_done_count = 0
                project.task_canceled_count = 0
                continue
            
            # Count tasks by state using filtered - matching your actual states
            project.task_in_progress_count = len(project.task_ids.filtered(lambda t: t.state == '01_in_progress'))
            project.task_changes_requested_count = len(project.task_ids.filtered(lambda t: t.state == '02_changes_requested'))
            project.task_approved_count = len(project.task_ids.filtered(lambda t: t.state == '03_approved'))
            project.task_done_count = len(project.task_ids.filtered(lambda t: t.state == '1_done'))
            project.task_canceled_count = len(project.task_ids.filtered(lambda t: t.state == '1_canceled'))
