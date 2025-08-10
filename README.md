# Learning to Handle APIs with Python

This repository documents my journey in learning how to interact with web APIs using Python. As practical examples, I’m exploring the [GitHub API](https://docs.github.com/en/rest), working with file downloads, checking my IP address, and practicing file handling.

## What’s Inside

- [`GitHubAPI.py`](GitHubAPI.py): My main Python script for experimenting with API requests, parsing JSON, and handling errors using the GitHub API.
- [`downloadingFiles.py`](downloadingFiles.py): Demonstrates how to download files from a URL with progress tracking and error handling.
- [`knowYourIP.py`](knowYourIP.py): Simple script to fetch and display your public IP address using the ipify API.
- [`fileHandling.py`](fileHandling.py): Practice file operations in Python, including reading, writing, appending, and searching for words in files.

## Getting Started

### Prerequisites

- Python 3.x
- [`requests`](https://pypi.org/project/requests/) library
- [`tqdm`](https://pypi.org/project/tqdm/) library (for download progress bar)

Install the required packages:

```sh
pip install requests tqdm
```

### How I Use the Scripts

- **GitHub API:**  
  Set the `username` variable in [`GitHubAPI.py`](GitHubAPI.py) to the GitHub profile you want to explore, then run:
  ```sh
  python GitHubAPI.py
  ```

- **Download Files:**  
  Run [`downloadingFiles.py`](downloadingFiles.py), paste a direct download URL when prompted, and the file will be saved as `video.mp4` with a progress bar:
  ```sh
  python downloadingFiles.py
  ```

- **Know Your IP:**  
  Run [`knowYourIP.py`](knowYourIP.py) to display your public IP address:
  ```sh
  python knowYourIP.py
  ```

- **File Handling Practice:**  
  Explore various file operations in [`fileHandling.py`](fileHandling.py) by uncommenting and running different code blocks.

## What I’m Learning

- Sending GET and POST requests to REST APIs using Python
- Parsing JSON responses from APIs
- Handling errors and displaying useful messages
- Downloading files with progress indication and robust error handling
- Reading, writing, and searching within files

## Quick Walkthroughs

### `GitHubAPI.py`
- **`get_user_info(username)`**: Fetches and prints basic info about a GitHub user (name, bio, repo count, followers, following).
- **`get_repos(username)`**: Lists all public repositories for the user.
- Both functions handle errors gracefully and print helpful messages if something goes wrong.

### `downloadingFiles.py`
- Prompts for a file URL, downloads the file with a progress bar, and handles errors professionally.

### `knowYourIP.py`
- Fetches and prints your public IP address in JSON format.

### `fileHandling.py`
- Contains examples for writing, reading, appending, and searching text in files.

## Example Output

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

1. Applying these in my upcoming project.
2. Experiment with other APIs and file operations to build my Python skills.

---

Thanks for checking out my API and file handling learning project!