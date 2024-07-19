import requests

def fetch_principal_assignments():
    url = 'http://localhost:5000/principal/assignments'
    headers = {'X-Principal-ID': '12'}

    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == '__main__':
    assignments = fetch_principal_assignments()
    print(assignments)
