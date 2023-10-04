import requests
import pytest

host = "https://api.pokemonbattle.me:9104"

def test_status_code():
    information_on_trainers = requests.get (f'{host}/trainers', params = {'level' : 1, 'trainer_id' : 1584})
    assert information_on_trainers.status_code == 200


def test_part_of_body():
    response = requests.get(f'{host}/trainers',
                            params = {'trainer_id' : 1584})
    assert response.json()["trainer_name"] == "Александр2000"



@pytest.mark.parametrize('key, value', [("trainer_name", "Александр2000"),
                                        ("id", "1584"),
                                        ("city", "Ставрополь")])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers',
                            params = {'trainer_id' : 1584})
    assert response.json()[key] == value