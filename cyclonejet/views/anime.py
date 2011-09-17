# -*- encoding:utf-8 -*-
from flask import Blueprint
from cyclonejet.models.anime import Anime
from cyclonejet.views.generic import PaginatedListView

anime = Blueprint('anime', __name__)

index = PaginatedListView.as_view('anime_list', template_name='entry-index.html', model=Anime)
anime.add_url_rule('/', view_func=index)

