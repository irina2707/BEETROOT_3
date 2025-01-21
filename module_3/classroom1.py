# import  requests
# url='https://api.chucknorris.io/jokes/random'
# response= requests.get(url)
# print(response.json())

# import requests
# url= 'https://api.chucknorris.io/jokes/categories'
# response=requests.get(url)
# print(response.json())

# import requests
# url='https://api.chucknorris.io/jokes/random?category=animal'
# response=requests.get(url)
# print(response.json())


# import requests
# response = requests.get('https://restcountries.com/v3.1/name/ukraine')
# data = response.json()
# # print()
# print(f"Столиця: {data[0]['capital'][0]}")

# import requests
# response = requests.get('https://restcountries.com/v3.1/region/europe')
# data = response.json()
# print(data)
# # print(f"Столиця: {data[0]['capital'][0]}")

# import requests

# categories_url='https://api.chucknorris.io/jokes/categories'

# categories_response=requests.get(categories_url)

# if categories_response.status_code in (200,201,202):
  
#   categories=categories_response.json()
#   print("Доступні категорії:")
#   print(" , ".join(categories))
# else:
#   print(f"Status_cod:{categories_response.status_code }")

# choose_category=input("Введіть  категорію:")
# if choose_category in categories:
#     joke_url=f'https://api.chucknorris.io/jokes/random?category={choose_category}'
#     joke_response=requests.get(joke_url)
#     if joke_response.status_code in (200,201,202):
#       joke=joke_response.json()
#       print(f"Жарт з категорії '{choose_category}':")
#       print(joke['value'])
#     else:
#        print(f"Status_cod:{categories_response.status_code }") 
# else:
#   print(f"Категорія '{choose_category}'недоступна.")  


# import requests
# response = requests.get(https://restcountries.com/v3.1/all)
# print(response)
# for country in countries:
#   if country_response.status_cod in (200,201,202):
#    country_response=requests.get('https://restcountries.com/v3.1/name/{country}')
#    print(f"Country is '{country}':")
#    print (f"Столиця: {data[0]['capital'][0]}")
#   else:
#     print("Error")


import requests

def search_country(country_name):
    # Format the URL with the provided country name
    country_url = f'https://restcountries.com/v3.1/name/{country_name}'
    
    # Make the GET request
    response = requests.get(country_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response and return it
        country_data = response.json()
        return country_data  # Return the parsed data
    else:
        # Return error message if the request fails
        return f"Failed to fetch data for {country_name}. Status code: {response.status_code}"

# Example usage
country_info = search_country('Germany')
print(country_info)
