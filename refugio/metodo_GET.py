
import requests
import json

def get_pokemons(url ='https://pokeapi.co/api/v2/pokemon-form/', offset = 0):
	args = {'offset': offset} if offset else {}
	response = requests.get(url, params=args)

	if response.status_code == 200:
			payload = response.json()
			results = payload.get('results', [])

			if results:
				for pokemon in results:
					name = pokemon['name']
					print(name)
			next = input('Continuar listando? [y/n]').lower()
			if next == 'y':
				get_pokemons(offset= offset+20)

def get_info_pokemon(url= 'https://pokeapi.co/api/v2/pokemon-form/', id =0 ):
	args = {'id': id} if id else {}
	id = input('Ingresa un ID', )
	print('El id que ingresaste es ',id)
	response = requests.get(url, params=args)
	print(response.url)


# if __name__ == '__main__':
# 	url = 'https://pokeapi.co/api/v2/pokemon-form/'
	# response = requests.get(url)
	# if response.status_code == 200:
	# 	payload = response.json()
	# 	results = payload.get('results', []) ## Este metodo intentara obtener la llave resultados y si no existe mostrara una lista vacia
	# 	if results:
	# 		for pokemon in results:
	# 			name = pokemon['name']
	# 			print(name)

	# get_pokemons()
	# id = input('Ingresa un ID', )
	# print('El id que ingresaste es ',id)
	# response = requests.get(url, id)
	# print(response.url)
if __name__ == '__main__':
	url = 'https://httpbin.org/delete'
	payload = {'nombre':'Eduardo', 'curso':'python'}
	headers = {'Content-Type':'application/json', 'access-token':'12345'}

	response = requests.delete(url, data = json.dumps(payload), headers= headers)
	print(response.url)

	if response.status_code == 200:
		##print(response.content)
		headers_response = response.headers
		server = headers_response['date']
		print(server)