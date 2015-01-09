from openerp import api,models,fields


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
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]

    @api.one
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

