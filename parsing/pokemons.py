import json
import requests
import pandas as pd


url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)

if response.status_code != 200: 
    print(response.text)
else:
    data = response.json()
    a = (data["count"])
    
response2 = requests.get(url, {'limit': a})

if response2.status_code != 200: 
    print(response2.text)
else:
    lst = response2.json()
ans = []

for j in lst["results"]:
    ans.append(j["name"])
    
answer = []
diction = {}
columns = []
counter = 0

for i in ans:
    name_or_id = i
    url = "https://pokeapi.co/api/v2/pokemon-species/{}/".format(name_or_id)
    response = requests.get(url, allow_redirects=True,headers={
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"
})
    if response.status_code == 200: 
        d = response.json()
        
        if d["is_legendary"]:
            answer.append(i)
            counter += 1
            
            for j in d:
                columns.append(j)
                
        diction[i] = d
        
df = pd.DataFrame(diction)
df.to_csv("result.csv", index=False)
df.head()
df = df.T
df.head()

df = df.query("is_legendary == True")
df["color"] = df["color"].apply(lambda x: x['name'])
df["egg_groups_name"] = df["egg_groups"].apply(lambda x: x[0]['name'])
df["egg_groups"] = df["egg_groups"].apply(lambda x: x[0]['url'])
df["evolution_chain"] = df["evolution_chain"].apply(lambda x: x['url'])
df["flavor_text_entries"] = df["flavor_text_entries"].apply(lambda x: x[0]['flavor_text'])
df["form_descriptions"] = df["form_descriptions"].apply(lambda x:  x[0]['description'] if len(x) > 0 else "-")
df["genera_genus"] = df["genera"].apply(lambda x:  x[0]['genus'])
df["genera_lang"] = df["genera"].apply(lambda x:  x[0]['language']['name'])
df["genera"] = df["genera"].apply(lambda x:  x[0]['language']['url'])
df["generation_name"] = df["generation"].apply(lambda x:  x['name'])
df["generation"] = df["generation"].apply(lambda x:  x['url'])
df["growth_rate_name"] = df["growth_rate"].apply(lambda x:  x['name'])
df["growth_rate"] = df["growth_rate"].apply(lambda x:  x['url'])

def f(x):
    if type(x) == dict:
        return(x["name"])
        
df["habitat_name"] = df["habitat"].apply(f)

def f1(x):
    if type(x) == dict:
        return(x["url"])
        
df["habitat"] = df["habitat"].apply(f1)
df["names_name"] = df["names"].apply(lambda x: x[0]["name"])
df["names_language"] = df["names"].apply(lambda x: x[0]["language"]["name"])
df["names"] = df["names"].apply(lambda x: x[0]["language"]["url"])

def f2(x):
    if len(x)!= 0:
        return(x[0]["base_score"])
        
df["pal_park_encounters_base_score"] = df["pal_park_encounters"].apply(f2)

def f3(x):
    if len(x)!= 0:
        return(x[0]["rate"])
        
df["pal_park_encounters_rate"] = df["pal_park_encounters"].apply(f3)

def f4(x):
    if len(x) != 0:
        return(x[0]["area"]["name"])
        
df["pal_park_encounters_name"] = df["pal_park_encounters"].apply(f4)

def f5(x):
    if len(x) != 0:
        return(x[0]["area"]["url"])
        
df["pal_park_encounters"] = df["pal_park_encounters"].apply(f5)
df["shape_name"] = df["shape"].apply(lambda x:  x['name'])
df["shape"] = df["shape"].apply(lambda x:  x['url'])
def f6(x):
    return(x[0]["entry_number"])
df["pokedex_numbers_entry"] = df["pokedex_numbers"].apply(f6)

def f7(x):
    return(x[0]["pokedex"]["name"])
df["pokedex_numbers_name"] = df["pokedex_numbers"].apply(f7)
def f6(x):
    return(x[0]["pokedex"]["url"])
df["pokedex_numbers"] = df["pokedex_numbers"].apply(f6)
def f6(x):
    return(x[0]["is_default"])
df["varieties_is_default"] = df["varieties"].apply(f6)

def f6(x):
    return(x[0]["pokemon"]["name"])
df["varieties_pokemon"] = df["varieties"].apply(f6)

def f6(x):
    return(x[0]["pokemon"]["url"])
df["varieties"] = df["varieties"].apply(f6)
pd.set_option('display.max_columns', None)
df.head(52)
df.to_csv("answer.csv", index=False)

