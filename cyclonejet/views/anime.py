# -*- encoding:utf-8 -*-
from flask import Blueprint, url_for, redirect, abort, flash, session, request, render_template

from cyclonejet.forms import RegistrationForm, LoginForm
from cyclonejet.models.anime import Anime
from cyclonejet.extensions import db

anime = Blueprint('anime', __name__)

@anime.route('/', methods=['GET'])
def index():
    """ Return an index of all collected animes. """

    NUM_PER_PAGE = 25

    page = int(request.args.get('p', 1))
    num_pages = (Anime.query.count() / NUM_PER_PAGE)
    
    if Anime.query.count() % NUM_PER_PAGE > 0:
        num_pages += 1

    if page < 1 or page > num_pages:
        return abort(404)

    animes = Anime.query.order_by('title').limit(NUM_PER_PAGE).offset((page-1)*NUM_PER_PAGE)

    return render_template('entry-index.html',
        entries = animes,
        current_page = page,
        num_pages = num_pages
    )

