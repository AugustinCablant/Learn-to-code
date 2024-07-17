import requests
import pandas as pd

# Remplacez par vos informations
client_id = '130587'
client_secret = '1969bdd5b2b51e2d0205f59a3e33d3e157786487'
refresh_token = 'e986e6ea7364e4af4743160ab9c2e1bb3b3831f3'

# Obtenir un jeton d'accès
auth_url = 'https://www.strava.com/oauth/token'
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': 'refresh_token',
    'f': 'json'
}

response = requests.post(auth_url, data=payload, verify=False)
access_token = response.json()['access_token']
print('Access Token:', access_token)

# Récupérer les activités
activities_url = 'https://www.strava.com/api/v3/athlete/activities'
headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(activities_url, headers=headers)
activities = response.json()

# Convertir en DataFrame pandas
df_activities = pd.DataFrame(activities)
print(df_activities.head())
