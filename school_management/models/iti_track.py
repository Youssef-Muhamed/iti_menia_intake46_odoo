from odoo import models, fields

class ItiTrack(models.Model):
    _name = 'iti.track'
    _rec_name = 'title'

    title = fields.Char(string='Title')
    student_ids = fields.One2many('iti.student', 'track_id', string='Students')
    duration = fields.Integer(string='Duration')