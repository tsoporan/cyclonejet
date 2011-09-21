# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template
from cyclonejet.models.manga import Manga
from cyclonejet.views.generic import PaginatedListView

manga = Blueprint('manga', __name__)

index = PaginatedListView.as_view('anime_list', template_name='manga/list.html', model=Manga)

def detail(manga_id):
    manga = Manga.query.get_or_404(manga_id)
    return render_template('manga/detail.html', manga=manga)

manga.add_url_rule('/', 'index', view_func=index)
manga.add_url_rule('/<int:manga_id>/', 'detail', view_func=detail)

