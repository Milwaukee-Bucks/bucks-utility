import os
import requests

# Directory structure
base_dir = 'color'
light_dir = os.path.join(base_dir, 'light', 'svg')
dark_dir = os.path.join(base_dir, 'dark', 'svg')

# Create directories if they don't exist
os.makedirs(light_dir, exist_ok=True)
os.makedirs(dark_dir, exist_ok=True)

# Team slugs and IDs
teams = {
    'hawks': '1610612737',
    'celtics': '1610612738',
    'nets': '1610612751',
    'hornets': '1610612766',
    'bulls': '1610612741',
    'cavaliers': '1610612739',
    'mavericks': '1610612742',
    'nuggets': '1610612743',
    'pistons': '1610612765',
    'warriors': '1610612744',
    'rockets': '1610612745',
    'pacers': '1610612754',
    'clippers': '1610612746',
    'lakers': '1610612747',
    'grizzlies': '1610612763',
    'heat': '1610612748',
    'bucks': '1610612749',
    'timberwolves': '1610612750',
    'pelicans': '1610612740',
    'knicks': '1610612752',
    'thunder': '1610612760',
    'magic': '1610612753',
    '76ers': '1610612755',
    'suns': '1610612756',
    'trail_blazers': '1610612757',
    'kings': '1610612758',
    'spurs': '1610612759',
    'raptors': '1610612761',
    'jazz': '1610612762',
    'wizards': '1610612764'
}

# Base URL for SVG logos
base_url = 'https://cdn.nba.com/logos/nba/{team_id}/primary/{variant}/logo.svg'

# Variants
variants = {
    'light': 'L',
    'dark': 'D'
}

for team_slug, team_id in teams.items():
    for variant_name, variant_letter in variants.items():
        url = base_url.format(team_id=team_id, variant=variant_letter)
        response = requests.get(url)

        if response.status_code == 200:
            file_path = os.path.join(
                light_dir if variant_name == 'light' else dark_dir,
                f'{team_slug}_{variant_name}.svg'
            )

            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Successfully downloaded {file_path}')
        else:
            print(f'Failed to download {url}')

print('Download completed.')

