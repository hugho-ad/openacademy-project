from openerp import models,fields, models


"""
This is a module that create the model of Course
"""

class Course(models.Model):
    """
    This class create a model class of Course
    """
    _name = 'openacademy.course' # String tomado por odoo 
                                 #para crear tabla en postgres

    name = fields.Char(string="Title", required=True) # Campo a generarse en la tabla _name
    description = fields.Text()# campo de tipo Text para almacenar strings multilineas
    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsible", index=True)
    sessions_ids = fields.One2many('openacademy.session','course_id',string="Sessions")
