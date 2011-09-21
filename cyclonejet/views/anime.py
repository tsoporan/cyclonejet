# -*- encoding:utf-8 -*-
from flask import Blueprint, request, render_template, session, jsonify, redirect, url_for
from cyclonejet.models.anime import Anime
from cyclonejet.models.votes import AnimeVote
from cyclonejet.models.users import User
from cyclonejet.views.generic import PaginatedListView
from cyclonejet.views.utils import login_required

from cyclonejet.extensions import db

anime = Blueprint('anime', __name__)

index = PaginatedListView.as_view('anime_list', template_name='anime/list.html', model=Anime)

def detail(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    return render_template('anime/detail.html', anime=anime)

@login_required
def vote(anime_id):
  
    #expect ajax request
    if request.is_xhr:
        if request.method == 'POST' and 'score' in request.form:
    
            user = User.query.get(session['uid']) 
            anime = Anime.query.get_or_404(anime_id)
            score = request.form.get('score', 0, type=float)
            vote = AnimeVote(
                score = score,
                user = user,
                anime= anime
            )
            db.session.add(vote)
            db.session.commit()

            return jsonify(success=True, score=score)

    else:
        return redirect(url_for('anime.detail', anime_id=anime_id))
vote.methods = ['POST']

anime.add_url_rule('/', 'index', view_func=index)
anime.add_url_rule('/<int:anime_id>/', 'detail', view_func=detail)
anime.add_url_rule('/<int:anime_id>/vote/', 'vote', view_func=vote)
