import tkinter as tk
import subprocess 

def select_all(event):
    url.select_range(0, tk.END)
    return "break" 

def check_yt_dlp():
    try:
        import yt_dlp
        return True
    except ImportError:
        return False

def download():

    if not check_yt_dlp():
            label.config(text="yt-dlp isn't installed. Installling dependency...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)
                label.config(text="Success by installing yt-dlp. Starting download...")
            except:
                label.config(text="Error by installing yt-dlp.")    
    video_url = url.get()
    selected_format = selected.get()
    try:
        if selected_format == "mp3":
            result = subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', video_url], check=True)
            output = result.stdout
            error = result.stderr
            
            if result.returncode == 0:
                label.config(text="Download completed!")
            else:
                label.config(text=f"Error: {error}")
        else:
            subprocess.run(['yt-dlp', '-f', 'bv*+ba', '--merge-output-format', selected_format, video_url], check=True)
        label.config(text="Download complete!")
    except subprocess.CalledProcessError:
        label.config(text="Error downloading video.")  

# window config
root = tk.Tk()
root.title("Video downloader")
root.geometry("400x300")
root.config(padx=20, pady=20)

# elements
selected = tk.StringVar(root)
selected.set("mp4")

label = tk.Label(root, text="Insert the url:", font=("Arial", 14))
label.pack(padx=15, pady=15)

url = tk.Entry(root, width=40)
url.pack(padx=15, pady=15)

video_format = tk.OptionMenu(root, selected, "mp4", "mp3")
video_format.pack(padx=15, pady=15)

button = tk.Button(root, text="Submit", command=download)
button.pack(padx=15, pady=15)

root.bind("<Control-a>", select_all)

root.mainloop()
