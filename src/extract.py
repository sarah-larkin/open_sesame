from config import API_URL
import requests

def extract_products():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()