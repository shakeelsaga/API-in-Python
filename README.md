# Learning to Handle APIs with Python

This repository documents my journey in learning how to interact with web APIs using Python. As a practical example, I’m exploring the [GitHub API](https://docs.github.com/en/rest) to fetch user information and repositories.

## What’s Inside

- [`GitHubAPI.py`](GitHubAPI.py): My main Python script for experimenting with API requests, parsing JSON, and handling errors.

## Getting Started

### Prerequisites

- Python 3.x
- [`requests`](https://pypi.org/project/requests/) library

Install the required package:

```sh
pip install requests
```

### How I Use the Script

1. I set the `username` variable in [`GitHubAPI.py`](GitHubAPI.py) to the GitHub profile I want to explore.
2. I run the script from the terminal:

    ```sh
    python GitHubAPI.py
    ```

## What I’m Learning

- Sending GET requests to REST APIs using Python
- Parsing JSON responses from APIs
- Handling errors and displaying useful messages

## Quick Walkthrough of `GitHubAPI.py`

- **`get_user_info(username)`**: Fetches and prints basic info about a GitHub user (name, bio, repo count, followers, following).
- **`get_repos(username)`**: Lists all public repositories for the user.
- Both functions handle errors gracefully and print helpful messages if something goes wrong.

Here’s a sample output:

```
User Information for billy:
Name: Billy
Bio: Python Developer
Public Repos: 10
Followers: 50
Following: 5

Repositories for user billy:
Total repositories: 10
- repo1
- repo2
...
```

## Next Steps in My Learning

- Try different usernames to see various profiles.
- Extend the script to fetch more details (like starred repos).
- Experiment with other APIs to build my Python skills.

---

Thanks for checking out my API