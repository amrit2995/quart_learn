#request_example.py
import requests
def query_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
def get_hero_names(filter=None):
    url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
    json_body = query_url(url)
    for member in json_body.get("members", []):
        if filter(member):
            yield member["name"]
def format_heroes_over(age=0):
    hero_names = get_hero_names(filter=lambda hero: hero.get("age", 0) > age)
    formatted_text = ""
    for hero in hero_names:
        formatted_text += f"{hero} is over {age}\n"
    return formatted_text
if __name__ == "__main__":
    print(format_heroes_over(age=30))