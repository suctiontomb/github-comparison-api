from fastapi import APIRouter, HTTPException
from github_api.services import fetch_github_user,compare_users
from github_api.models import GitHubUser

router = APIRouter()

@router.get("/users/{username}")
def get_user(username: str) -> GitHubUser:
    """Fetch a single GitHub user."""
    user = fetch_github_user(username)
    if user is None:
        raise HTTPException(status_code =404, detail="user not found")
    return user

@router.get("/compare/{user1}/{user2}")
def compare_github_user(user1: str, user2: str) -> dict:
    """compare two Github users."""
    result = compare_users(user1,user2)
    if result is None:
        raise HTTPException(status_code=404, detail="One or both users not found")
    return result

@router.get("/users")
def get_interesting_users() -> list[str]:
    """Returns a list of interesting GitHub users to compare."""
    return [
        "torvalds",
        "gvanrossum",
        "kennethreitz",
        "django",
        "suctiontomb"

    ]





