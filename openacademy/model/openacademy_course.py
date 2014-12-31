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
    description = fields.Text()
