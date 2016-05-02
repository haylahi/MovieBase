# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import *

class AddMovieWizard(models.TransientModel):
    _name = 'moviedatabase.addmoviewizard'

    movie_titles = fields.Many2one('moviedatabase.movie', required = True, string="Movie")
    movie_actor_id = fields.Many2one('moviedatabase.movie', string="Actors")
