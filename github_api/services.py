from unittest import result

from github_api.models import GitHubUser
import requests

def fetch_github_user(username: str) -> GitHubUser | None:
    """ Fetches data of given username from Github """
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 404:
        return None

    data = response.json()
    result = GitHubUser(username= data['login'],
                        name= data['name'],
                        public_repos= data['public_repos'],
                        followers= data['followers'],
                        created_at=data['created_at']
    )

    return result

def compare_users(user1: str, user2: str) -> dict | None:
    """Compares two GitHub users and returns comparison result."""
    first_user = fetch_github_user(user1)
    second_user = fetch_github_user(user2)

    if first_user is None or second_user is None:
        return None

    most_followers = get_winner(first_user.followers, second_user.followers, first_user.name, second_user.name)
    most_repos = get_winner(first_user.public_repos, second_user.public_repos, first_user.name, second_user.name)

    return {
        'user1': first_user.model_dump(),
        'user2': second_user.model_dump(),
        'most_followers': most_followers,
        'most_repos': most_repos
    }

def get_winner(val1: int,val2: int, name1: str, name2: str) -> str:
    """compares values and returns the name with the most"""
    if val1 > val2: return name1
    elif val2 > val1: return name2
    else: return f"{name1}, {name2}"






