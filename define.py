import json
import requests
import sys

api_url = "https://api.dictionaryapi.dev/api/v2/entries/en"

def search_word(word):
    return requests.get(f"{api_url}/{word}")

def print_meanings(meanings):
	for i in meanings:
		print(f"({i['partOfSpeech']})")
		for j in i["definitions"]:
			print(f"\t- {j['definition']}")

def main():
	if len(sys.argv) > 1:
		word = sys.argv[1]
	else:
		print("No word given")
		sys.exit(1)
	
	api_response = search_word(word)
	if api_response.status_code == 404:
		print("Definition not found")
		sys.exit(2)
	
	meanings = api_response.json()[0]["meanings"]
	print_meanings(meanings)

if __name__ == "__main__":
	main()
