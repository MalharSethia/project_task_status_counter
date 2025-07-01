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
    
    # Percentage fields for tooltips
    task_in_progress_percent = fields.Char(
        string='In Progress Percentage',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_changes_requested_percent = fields.Char(
        string='Changes Requested Percentage', 
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_approved_percent = fields.Char(
        string='Approved Percentage',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_done_percent = fields.Char(
        string='Done Percentage',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_canceled_percent = fields.Char(
        string='Canceled Percentage',
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
                project.task_in_progress_percent = "0%"
                project.task_changes_requested_percent = "0%"
                project.task_approved_percent = "0%"
                project.task_done_percent = "0%"
                project.task_canceled_percent = "0%"
                continue
            
            total_tasks = len(project.task_ids)
            
            # Count tasks by state using filtered - matching your actual states
            in_progress_count = len(project.task_ids.filtered(lambda t: t.state == '01_in_progress'))
            changes_requested_count = len(project.task_ids.filtered(lambda t: t.state == '02_changes_requested'))
            approved_count = len(project.task_ids.filtered(lambda t: t.state == '03_approved'))
            done_count = len(project.task_ids.filtered(lambda t: t.state == '1_done'))
            canceled_count = len(project.task_ids.filtered(lambda t: t.state == '1_canceled'))
            
            # Set counts
            project.task_in_progress_count = in_progress_count
            project.task_changes_requested_count = changes_requested_count
            project.task_approved_count = approved_count
            project.task_done_count = done_count
            project.task_canceled_count = canceled_count
            
            # Calculate percentages
            if total_tasks > 0:
                project.task_in_progress_percent = f"In Progress: {in_progress_count} ({round((in_progress_count / total_tasks) * 100)}%)"
                project.task_changes_requested_percent = f"Changes Requested: {changes_requested_count} ({round((changes_requested_count / total_tasks) * 100)}%)"
                project.task_approved_percent = f"Approved: {approved_count} ({round((approved_count / total_tasks) * 100)}%)"
                project.task_done_percent = f"Done: {done_count} ({round((done_count / total_tasks) * 100)}%)"
                project.task_canceled_percent = f"Canceled: {canceled_count} ({round((canceled_count / total_tasks) * 100)}%)"
            else:
                project.task_in_progress_percent = "0%"
                project.task_changes_requested_percent = "0%"
                project.task_approved_percent = "0%"
                project.task_done_percent = "0%"
                project.task_canceled_percent = "0%"
