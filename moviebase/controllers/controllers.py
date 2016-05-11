# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import *

# from imdb import IMDb ===> TEST THIS

class MovieDatabase(models.Model):
    _name = 'moviedatabase.database'
    _description = "Movie Database"


class Movie(models.Model):
    _name = "moviedatabase.movie"
    _rec_name = 'title'

    title = fields.Char(string="Title", required=True)
    duration = fields.Float(string="Duration")               # use widget="float_time" for displaying
    release_year = fields.Selection([(num, str(num)) for num in range(1900, (datetime.now().year)+1 )], string="Release Year")
    filepath = fields.Char(string="File Path")
    to_be_released = fields.Boolean(string="In Production")
    file_format = fields.Selection([(1, "AVI"),(2, "WMA"),(3, "MKV"),(4, "M4V"),])
    genre = fields.Selection([(1, "Comedy"),(2, "Sci-Fi"),(3, "Animation"),(4, "Drama"),(5, "Thriller"),(6, "Horror")])
    movie_actors_ids = fields.One2many('moviedatabase.people', 'person_id', string="Actors")

class People(models.Model):
    _name = "moviedatabase.people"
    _rec_name = 'person_name'

    person_id = fields.Many2many('moviedatabase.movie', string="Acted In")
    person_name = fields.Char(string="Name")
    person_age = fields.Float(string="Age")
    is_actor = fields.Boolean(string="Actor")
    is_director = fields.Boolean(string="Director")
