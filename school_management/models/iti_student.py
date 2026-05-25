from odoo import models, fields,api,_
from odoo.exceptions import ValidationError

class ItiStudent(models.Model):
    _name = 'iti.student'
    _description = 'ITI Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'name'

    #to prevent logging access for this model
    # _log_access = False

    name = fields.Char(string='Name',tracking=True)
    email = fields.Char(string='Email',tracking=True)
    description = fields.Text(string='Description')
    birthday = fields.Datetime(string='Birthday')
    age = fields.Integer(string='Age',compute='_compute_age',store=True)
    notes = fields.Html(string='Notes')
    is_graduated = fields.Boolean(string='Is Graduated')
    salary = fields.Float(string='Salary')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], string='Status',default='draft', tracking=True)

    track_id = fields.Many2one(comodel_name='iti.track', string='Track',domain="[('duration','>',5)]")
    message = fields.Char(string='Message')
    skills_ids = fields.Many2many(comodel_name='iti.skill', string='Skills')
    duration = fields.Integer(related='track_id.duration',store=True)

    _name_uniq = models.Constraint(
        'unique(name)',
        'The name must be unique!',
    )

    @api.constrains('salary')
    def _check_salary(self):
        for record in self:
            if record.salary < 1000:
                raise ValidationError(_("Salary must be greater than 1000"))

    @api.onchange('track_id')
    def _onchange_track_id(self):
        print('------>onchange', self)
        self.message = "Track is changed to %s" % self.track_id.title
        # self.message = f"Track is changed to {self.track_id.title}"
        return {
            'warning': {'title': "Warning", 'message': "Track is changed", 'type': 'notification'},
        }

    @api.depends('birthday')
    def _compute_age(self):
        print('------>', self)
        for record in self:
            if record.birthday:
                today = fields.Date.today()
                record.age = (today - fields.Date.from_string(record.birthday)).days // 365

    def action_accept(self):
        self.status = 'accepted'

    def action_set_draft(self):
        self.status = 'draft'

    def action_rejected(self):
        self.status = 'rejected'

    @api.model
    def create(self, vals):
        # for val in vals:
        #     val['email'] = val['email'] + '@gmail.com'
        return super(ItiStudent, self).create(vals)

    def write(self, vals):
        print('------>write', vals)
        return super(ItiStudent, self).write(vals)

    def copy(self, default=None):
        print('------>copy', default)
        return super(ItiStudent, self).copy(default)

    def unlink(self):
        print('------>unlink', self)
        return super(ItiStudent, self).unlink()


# python inheritance
# model inheritance
# view inheritance