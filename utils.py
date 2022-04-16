import json


def load_candidates(path):
    with open(path, 'r', encoding='utf-8') as candidates_file:
        return json.load(candidates_file)


def pattern_candidates(candidates_list):
    views = '<pre>'
    for candidate in candidates_list:
        views += (
            f'Имя кандидата -     {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки кандидата -  {candidate["skills"]}\n\n'
        )
    views += '<pre>'
    return views


def sort_by_id(candidates_list, candidate_id):
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def sort_by_skill(candidates_list, candidate_skill):
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if candidate_skill in candidate_skills:
            result.append(candidate)

    return result
