from odoo import models, fields, api

class CreateTrack(models.TransientModel):
    _name = 'create.track'
    _description = 'Create Track'

    title = fields.Char(string='Title')
    duration = fields.Integer(string='Duration')

    def action_create_track(self):
        vals = {
            'title': self.title,
            'duration': self.duration
        }
        track = self.env['iti.track'].create(vals)
        return track