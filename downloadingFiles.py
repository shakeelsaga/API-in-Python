import requests
from tqdm import tqdm

# url = "https://videos.pexels.com/video-files/32200340/13732776_2560_1440_60fps.mp4"
# url = "https://assets.mixkit.co/videos/41576/41576-2160.mp4"
url = input("Paste a URL to download the file:")
r = requests.get(url)


try:
    totalBytes = int(r.headers["Content-Length"])
    loading = tqdm(total = totalBytes, unit="iB", unit_scale = True)
    # bytesReceived = 0
    # bytesInMB = 0
    # totalInMB = totalBytes / 1000000
    with open ("video.mp4", 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            loading.update(128)
            # bytesInMB = bytesReceived/1000000;
            # totalInMB = totalBytes/1000000;
            # print(f"{bytesInMB:.2f} MB received out of total {totalInMB:.2f} MB", end="\r")
            f.write(chunk)
            # bytesReceived += 128
    print("Downloading Completed!")
except Exception:
    print("\nError: The file could not be downloaded. Please verify the URL and ensure it points to a direct downloadable resource.")
    print("Tip: Use links that provide direct download access, such as those from trusted sources or file hosting services.")

# bytesInMB = bytesReceived / 1000000
# totalInMB = totalBytes / 1000000
# print(f"{bytesInMB:.2f} MB received out of total {totalInMB:.2f} MB")