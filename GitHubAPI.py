import requests

base_url = "https://api.github.com"

def get_user_info(username):
    url = f"{base_url}/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_info = response.json()
        print(f"User Information for \033[1m{username}\033[0m:")
        print(f"Name: {user_info.get('name', 'N/A')}")
        print(f"Bio: {user_info.get('bio', 'N/A')}")
        print(f"Public Repos: {user_info.get('public_repos', 0)}")
        print(f"Followers: {user_info.get('followers', 0)}")
        print(f"Following: {user_info.get('following', 0)}")
    else:
        print(f"Failed to retrieve information for user {username}.")
        print("Please check the username or your network connection.")

def get_repos(username):
    url = f"{base_url}/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"Repositories for user \033[1m{username}\033[0m:")
        print(f"Total repositories: \033[1m{len(repos)}\033[0m")
        for repo in repos:
            print(f"- {repo['name']}")
    else:
        print(f"Failed to retrieve repositories for user {username}.")
        print("Please check the username or your network connection.")


username = "shakeelsaga"

get_user_info(username)
print("\n")
get_repos(username)

