import requests
import pandas as pd

print('llego......')
# URl básica
base_url = "https://prep2024.ine.mx/publicacion/nacional/assets/presidencia/entidad/{}.json"

# Dataframe en blanco
all_data = pd.DataFrame()

# Iterar por las 32 entidades
for id_entidad in range(1, 33):
    # url
    url = base_url.format(id_entidad)
    
    response = requests.get(url)
    data = response.json()

    # Extraer datos de los partidos
    votes_data = data['votosPartidosPoliticos']['votos']
    entidad = data['entidad']

    # Listas para almacenar votos por partido
    votos_pan = []
    votos_pri = []
    votos_prd = []
    votos_pvem = []
    votos_pt = []
    votos_mc = []
    votos_morena = []
    votos_no_reg = []
    votos_nulos = []

    # Extraer datos
    for vote in votes_data:
        if vote['partido'] == '1':
            votos_pan.append(vote['votos'])
        if vote['partido'] == '2':
            votos_pri.append(vote['votos'])
        if vote['partido'] == '3':
            votos_prd.append(vote['votos'])
        if vote['partido'] == '4':
            votos_pvem.append(vote['votos'])
        if vote['partido'] == '5':
            votos_pt.append(vote['votos'])
        if vote['partido'] == '6':
            votos_mc.append(vote['votos'])
        if vote['partido'] == '8':
            votos_morena.append(vote['votos'])
        if vote['partido'] == '61':
            votos_no_reg.append(vote['votos'])
        if vote['partido'] == '62':
            votos_nulos.append(vote['votos'])

    # Crear dataframe
    df = pd.DataFrame({
        'pan': votos_pan,
        'pri': votos_pri,
        'prd': votos_prd,
        'pvem': votos_pvem,
        'pt': votos_pt,
        'mc': votos_mc,
        'morena': votos_morena,
        'no_reg': votos_no_reg,
        'nulos': votos_nulos,
        'entidad': entidad
    })

    # Eliminar comas
    df = df.replace(',', '', regex=True).astype(int)

    # Pegar el dataframe al dataframe general
    all_data = pd.concat([all_data, df], ignore_index=True)
print(all_data)
