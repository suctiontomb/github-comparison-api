import requests

def get_github_user(username: str) -> dict | None:
    """
       Fetch a GitHub user's public profile data.

       Args:
           username: GitHub username to look up

       Returns:
           Dict with name, public_repos, followers, created_at
           None if user doesn't exist
       """
    
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 404:
        return None
    data = response.json()
    result = {'name': data['name'], 'public_repos': data['public_repos'], 'followers': data['followers'], 'created_at': data['created_at']}
    return result

def compare_users(user1,user2: str) -> list | None:
    """Compares two users and returns the user with the most followers, Public Repos ."""
    user1_data = get_github_user(user1)
    user2_data = get_github_user(user2)

    who_wins = ""
    if user2 is None and user1 is None:
        print("Both users do not exist, therefore we can't compare")
        return
    elif user2_data is None:
        print(f"User 2 doesn't exist. Most Followers: {user1_data['name']}, Most public repos: {user1_data['public_repos']}")
        return
    elif user1_data is None:
        print(f"User 1 doesn't exist. Most Followers: {user2_data['name']}, Most public repos: {user2_data['public_repos']}")
        return

    else:
        if user1_data['followers'] > user2_data['followers']:
            who_wins += f" {user1_data['name']} has the most followers."
        elif user2_data['followers'] > user1_data['followers']:
            who_wins += f" {user2_data['name']} has the most followers."
        else:
            who_wins  += f" Both users are equal in follower amount."

        if user1_data['public_repos'] > user2_data['public_repos']:
            who_wins += f" {user1_data['name']} has the most public repos."
        elif user2_data['public_repos'] > user1_data['public_repos']:
            who_wins += f" {user2_data['name']} has the most public repos."
        else:
            who_wins += f" Both users are equal in public repos amount."

    print(who_wins)