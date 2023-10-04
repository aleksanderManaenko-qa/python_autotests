import requests

token = "e4c36b344cc0a98e4ec2d56335094f37"

'''response_kill = requests.post ('https://api.pokemonbattle.me:9104/pokemons/kill', json = { 
    "pokemon_id" : "3451"}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(response_kill.text)



response_creat = requests.post ("https://api.pokemonbattle.me:9104/pokemons",
               json= {
              "name": "Аркаша",
              "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                headers = {"Content-Type" : "application/json", "trainer_token" : token})
print(response_creat.text)'''


'''response_rename = requests.patch ("https://api.pokemonbattle.me:9104/pokemons", 
    json = {
    "pokemon_id": "11789",
    "name": "Анатолий"}, 
    headers = {"Content-Type" : "application/json", "trainer_token" : token})
print (response_rename.text)'''


response_add_pokeball = requests.post ("https://api.pokemonbattle.me:9104/trainers/add_pokeball",
                                       json = {"pokemon_id": "11789"}, 
                                       headers = {"Content-Type" : "application/json", "trainer_token" : token})
print (response_add_pokeball.text)