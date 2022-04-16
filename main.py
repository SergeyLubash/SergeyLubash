from flask import Flask
from utils import load_candidates, pattern_candidates, sort_by_id, sort_by_skill

app = Flask(__name__)


@app.route('/')
def main():
    candidates_list = load_candidates('candidates.json')

    return pattern_candidates(candidates_list)


@app.route('/candidates/<int:candidate_id>')
def page_candidate(candidate_id):
    candidates_list = load_candidates('candidates.json')

    candidate = sort_by_id(candidates_list, candidate_id)
    picture = f'<img src ="{candidate["picture"]}">'
    return picture + pattern_candidates([candidate])


@app.route('/skills/<skill>')
def skills(skill):
    candidates_list = load_candidates('candidates.json')

    return pattern_candidates(sort_by_skill(candidates_list, skill))


app.run()
