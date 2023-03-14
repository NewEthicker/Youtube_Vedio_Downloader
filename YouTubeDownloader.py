from pytube import YouTube

while True:
    print("1. Download video by URL")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        url = input("Enter the YouTube video URL: ")
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        for i, stream in enumerate(streams):
            print(f"{i+1}. {stream}")
        choice = int(input("Enter the stream number to download: "))
        streams[choice-1].download()
        print("Video downloaded successfully.")
    elif choice == '2':
        exit()
    else:
        print("Invalid choice. Please try again.")
