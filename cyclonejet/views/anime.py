# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template
from cyclonejet.models.anime import Anime
from cyclonejet.views.generic import PaginatedListView

anime = Blueprint('anime', __name__)

index = PaginatedListView.as_view('anime_list', template_name='anime/list.html', model=Anime)

def detail(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    return render_template('anime/detail.html', anime=anime)


anime.add_url_rule('/', 'index', view_func=index)
anime.add_url_rule('/<int:anime_id>/', 'detail', view_func=detail)
