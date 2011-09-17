# -*- encoding:utf-8 -*-
from flask import Blueprint
from cyclonejet.models.manga import Manga
from cyclonejet.views.generic import PaginatedListView

manga = Blueprint('manga', __name__)

index = PaginatedListView.as_view('anime_list', template_name='entry-index.html', model=Manga)
manga.add_url_rule('/', 'index', view_func=index)

