from pydantic import BaseModel

class GitHubUser(BaseModel):
    username: str
    name: str
    public_repos: int
    followers: int
    created_at: str




