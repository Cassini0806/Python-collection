import requests
import os
from datetime import datetime

def fetch_data(endpoint, id=None, filters = {}):
    url = f"https://api.batmanapi.com/v1/{endpoint}"
    if id:
        url += f"/{id}"
    print("Searching results...")
    response = requests.get(url, params=filters)
    return response.json() if response.status_code == 200 else None

def formatation(lock):
    value = int(input("Enter file id: "))  
    item = fetch_data(lock, id=value)
    if item:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela no Windows ou Unix-based
        data = item["data"]
        att = data["attributes"]
        print(f"Name: {att["name"]}")
        print(f"Description: {att["description"]}")
        print('')
        if lock == "characters":
            print(f"Alias: {att["alias"]} // Role: {att["role"]}")
            print(f"Gender: {att["gender"]} // Alive: {att["alive"]}")
            print(f"Abilities: {att["abilities"]}")
            print('')
            print(f"First Appearance: {att["first_appearance"]} // Creator: {att["creator"]}")
        elif lock == "locations":
            print(f"Type: {att["type"]}")
            print(f"Coordinates: {att["coordinates"]}")
            print(f"Notable Events: {att["notable_events"]} // Related Characters: {att["related_characters"]}")
            print('')
            print(f"First Appearance: {att["first_appearance"]} // Creator: {att["creator"]}")
        elif lock == "concepts":
            print(f"Type: {att["type"]}")
            print(f"First Appearance: {att["first_appearance"]} // Creator: {att["creator"]}")
        elif lock == "storylines":
            print(f"Publication Date: {att["publication_date"]}")
            print(f"Writer: {att["writer"]} // Artist: {att["artist"]}")
            print(f"Issues: {att["issues"]}")
            print('')
            print(f"Characters: {att["characters"]} // Locations: {att["locations"]}")
    else:
        print("Failed to fetch data")
    	
def terminal():
    print("Available Archives")
    print("People = 0 // Locations = 1 // Concepts = 2 // Storylines = 3 // Exit = 4")
    key = input("Enter archive key: ")
    if key == "0":
        lock = "characters"
        formatation(lock)
    elif key == "1":
        lock = "locations"
        formatation(lock)
    elif key == "2":
        lock = "concepts"
        formatation(lock)
    elif key == "3":
        lock = "storylines"
        formatation(lock)
    elif key == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Key not found]")
        terminal()

def menu():
    key = input("What will you do today? ")
    if key == "help":
        print("Available Commands: clear, datetime, files, list, help")
        menu()
    elif key == "files":
        terminal()
        menu()
    elif key == "datetime":
        date = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(date)
        menu()
    elif key == "list":
        print("people ID: 83 | locations ID: 49 | concepts ID: 38 | storylines ID: 41")
        menu()
     elif key == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()

print(r"""
888888b.            888    888b     d888                          .d8888b.                    888                           
888  "88b           888    8888b   d8888                         d88P  Y88b                   888                           
888  .88P           888    88888b.d88888                         Y88b.                        888                           
8888888K.   8888b.  888888 888Y88888P888  8888b.  88888b.         "Y888b.   888  888 .d8888b  888888  .d88b.  88888b.d88b.  
888  "Y88b     "88b 888    888 Y888P 888     "88b 888 "88b           "Y88b. 888  888 88K      888    d8P  Y8b 888 "888 "88b 
888    888 .d888888 888    888  Y8P  888 .d888888 888  888             "888 888  888 "Y8888b. 888    88888888 888  888  888 
888   d88P 888  888 Y88b.  888   "   888 888  888 888  888       Y88b  d88P Y88b 888      X88 Y88b.  Y8b.     888  888  888 
8888888P"  "Y888888  "Y888 888       888 "Y888888 888  888        "Y8888P"   "Y88888  88888P'  "Y888  "Y8888  888  888  888 
                                                                                 888                                        
A Wayne Enterprises Software                                                Y8b d88P                                        
                                                                             "Y88P"                                         """)
print('')
menu()
