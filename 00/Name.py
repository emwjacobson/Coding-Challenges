import requests as r

if __name__ == '__main__':
    response = r.get('https://randomuser.me/api/?nat=US').json()
    print("Gender: {}\nName: {} {}\nAddress: {}, {}, {}\nEmail: {}\nPhone Number: {}\nUsername: {}\nPassword: {}"\
    .format(response['results'][0]['gender'],response['results'][0]['name']['first'],\
    response['results'][0]['name']['last'],response['results'][0]['location']['street'],\
    response['results'][0]['location']['city'],response['results'][0]['location']['state'],\
    response['results'][0]['email'],response['results'][0]['phone'],response['results'][0]['login']['username'],\
    response['results'][0]['login']['password']))
