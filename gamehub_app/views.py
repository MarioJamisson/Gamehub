from django.shortcuts import render
from django.http import HttpResponse
import os
import requests
from PIL import Image
from io import BytesIO
import unicodedata
import re

def index(request):
    return render(request, 'index.html')

def normaliza_nome(nome):
    nome = os.path.splitext(nome)[0]
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode()
    return nome.lower().replace(' ', '_')

def limpar_nome_jogo(nome):
    # Remove parênteses e tudo dentro
    nome = re.sub(r'\(.*?\)', '', nome)
    return nome.strip()

def get_igdb_cover(game_name, platform_id):
    game_name = limpar_nome_jogo(game_name)
    covers_dir = os.path.join('gamehub_app', 'static', 'covers')
    os.makedirs(covers_dir, exist_ok=True)

    nome_limpo = normaliza_nome(game_name)
    filename = f"{nome_limpo}.png"
    filepath = os.path.join(covers_dir, filename)

    if os.path.exists(filepath):
        return f"/static/covers/{filename}"

    client_id = 'u54eax7r0alow8vx2ks5b1ln4aet8q'
    client_secret = 'pt5rnjb8lgrume7doi6jt1ah66x6bk'

    try:
        token_resp = requests.post('https://id.twitch.tv/oauth2/token', data={
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials'
        })
        access_token = token_resp.json().get('access_token')

        headers = {
            'Client-ID': client_id,
            'Authorization': f'Bearer {access_token}',
        }

        data = f'''
            search "{game_name}";
            fields name, cover.image_id;
            where platforms = ({platform_id});
            limit 1;
        '''

        response = requests.post('https://api.igdb.com/v4/games', headers=headers, data=data)
        response_data = response.json()

        if response_data and 'cover' in response_data[0]:
            image_id = response_data[0]['cover']['image_id']
            url = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{image_id}.png"
            img_data = requests.get(url).content
            image = Image.open(BytesIO(img_data)).convert('RGB')
            image.save(filepath, format='PNG', optimize=True)
            return f"/static/covers/{filename}"

    except Exception as e:
        print(f"⚠️ Erro: {e}")

    return "/static/img/sem-capa.png"

def listar_jogos(request):
    if request.method == 'POST':
        pasta = request.POST.get('pasta')
        platform_id = request.POST.get('platform', '7')  # padrão: PS1

        if not pasta or not os.path.exists(pasta):
            return HttpResponse("Caminho inválido, bicho!")

        jogos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]
        jogos_com_capa = []

        for jogo in jogos:
            nome = os.path.splitext(jogo)[0]
            capa = get_igdb_cover(nome, platform_id)
            jogos_com_capa.append({
                'nome': nome,
                'capa': capa
            })

        context = {
            'jogos': jogos_com_capa,
            'tema': 'futurista',
            'gradiente': 'from-black via-gray-900 to-red-900'
        }
        return render(request, 'listar_jogos.html', context)

    return render(request, 'escolher_pasta.html')
