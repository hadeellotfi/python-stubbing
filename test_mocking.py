import requests #pip install requests

def add(a, b):
    return a+b 

def get_joke():
    url = 'http://api.icndb.com/jokes/random'
    response = requests.get(url)

    if response.status_code == 200: 
        joke = response.json()['value']['joke']
    else:
        joke = 'No jokes'
    
    return joke

# Func that have a dependancy 
def len_joke():
    joke = get_joke() 
    return len(joke)

if __name__ == '__main__':
    print(get_joke())