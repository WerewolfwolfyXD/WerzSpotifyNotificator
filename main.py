from theme_color_processor import get_theme_color
from network import *
import tkinter as tk
import webbrowser

from colorthief import ColorThief

import spotipy
import spotipy.util as util
from spotipy import SpotifyClientCredentials, SpotifyOAuth

window = tk.Tk()
window.geometry("500x500")

playing_status = False

spot = SpotifyOAuth(client_id="0268f4088917445cb0bc1039b15dd31b",
                    client_secret="b47486c742aa413785e08091e676f6e9",
                    redirect_uri="http://localhost:8879/callback",
                    scope="user-library-read user-follow-read user-top-read user-read-private playlist-read-private user-read-playback-state user-follow-modify user-library-modify playlist-modify-public playlist-modify-private",
                    )

f = open('token.bin', 'r')
tok = f.read()
at = spot.get_access_token(tok)
spc = spotipy.Spotify(auth=at["access_token"])
playing_volume = 100
toplevel_opacity = 0.9

def authentication():
    auth_url = spot.get_authorize_url()
    print(auth_url)
    webbrowser.open(auth_url)


def process_toplevel_opacity(entry):
    global toplevel_opacity
    toplevel_opacity = widgets_entry_toplevelopacity.get()

class ImageTextContainer(tk.Frame):
    def __init__(self, parent, image_path, text, colorful, **kwargs):
        super().__init__(parent, **kwargs)

        self.image_label = tk.Label(self)
        self.image_label.pack(side=tk.LEFT, padx=10, pady=10)

        # 加载图片
        self.byte_img = get_url_as_byte(image_path)
        self.byte_img = get_url_as_byte(image_path)
        self.byte_img_data = io.BytesIO(self.byte_img)
        self.kv_image = Image.open(self.byte_img_data)
        self.kz_image = self.kv_image.resize((200, 200), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.kz_image)
        self.image_label.config(image=self.tk_image)

        # # 创建滚动文本
        # self.text_widget = tk.Text(self, height=10, width=40)
        # self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.text_widget.insert(tk.END, text)
        self.label_songname = tk.Label(self, text=text["song_name"], font=("MiSans Bold", 30), justify='left',
                                       fg=colorful["ctext"], bg=colorful["ctheme"])
        self.label_songname.pack()

        self.label_album = tk.Label(self, text=f"""《{text["album_name"]}》 ({text["album_rdate"]})""",
                                    font=("MiSans Bold", 12), justify='left', fg=colorful["ctext"],
                                    bg=colorful["ctheme"])
        self.label_album.pack()

        self.label_artists = tk.Label(self, text=f"""By {text["song_artists_pure"]}""",
                                    font=("MiSans Bold", 12), justify='left', fg=colorful["ctext"],
                                    bg=colorful["ctheme"])
        self.label_artists.pack()

        self.label_current_device = tk.Label(self, text=text["current_device_pure"], font=("MiSans Bold", 12), justify='left',
                                       fg=colorful["ctext"], bg=colorful["ctheme"])
        self.label_current_device.pack()

        self.label_fake_play_status = tk.Label(self, text=f"🔁      ⏮️    ▶️    ⏭️      🔊", font=("MiSans Bold", 12),
                                             fg=colorful["ctext_pure"], bg=colorful["ctheme"])
        self.label_fake_play_status.pack()

        #
        # self.button_stop = tk.Button(self, text="⏸" if playing_status else "▶", command=stop_resume_play, fg=colorful["ctext"], bg=colorful["ctheme"])
        # self.button_stop.pack()
        #
        # self.button_volumne_50 = tk.Button(self, text="Volumne 50%", command=lambda:set_volume(50), fg=colorful["ctext"], bg=colorful["ctheme"])
        # self.button_volumne_50.pack()


def show_notification(message):
    # 创建一个新窗口
    root = tk.Toplevel()
    root.attributes("-topmost", True)  # 确保窗口总是在最前面
    root.overrideredirect(True)  # 移除窗口边框
    # root.wm_attributes('-transparentcolor', 'white')
    root.attributes('-alpha', toplevel_opacity)

    # 设置窗口的初始位置
    root.geometry(f"-1000+0")
    padx = 90

    theme_color = get_theme_color()

    lab = ImageTextContainer(root, message["img_url"], message["text"], colorful=theme_color, padx=padx, pady=5, bg=theme_color["ctheme"])
    lab.pack(fill=tk.BOTH, expand=True)

    # 定义动画函数，使窗口从屏幕外移动到右上角
    def animate_into():
        nonlocal padx
        nonlocal counter
        counter += 1

        animate_x = -padx * 2 + 10 * counter
        if animate_x >= 0:
            animate_x = 0

        animate_y = 20
        root.geometry(f"+{animate_x}+{animate_y}")
        if counter <= 250:
            root.after(10, animate_into)
        else:
            counter = 0
            root.after(10, animate_outro)

    def animate_outro():
        nonlocal padx
        nonlocal counter
        counter += 1

        animate_x = 0 - 12 * counter

        animate_y = 20
        root.geometry(f"+{animate_x}+{animate_y}")
        if animate_x >= -padx * 10:
            root.after(10, animate_outro)
        else:
            root.after(10, root.destroy())

    counter = 0

    # 启动动画
    root.after(0, animate_into)

    # 显示窗口
    root.deiconify()
    #
    # # 等待一段时间后自动关闭通知
    # root.after(5000, root.destroy)


def set_volume(vol):
    global playing_volumn
    spc.volume(20)


def stop_resume_play():
    global playing_status
    if playing_status:
        playing_status = False
        spc.pause_playback()
    else:
        playing_status = True
        spc.start_playback()
    print(f"RESUME ! {playing_status.__str__()}")


def processnow():
    pre_message = {}
    print(at)
    print(spc.devices())

    current_username = spc.current_user()["display_name"]

    current_devices = spc.devices()
    current_devices_text = ""
    for i in current_devices["devices"]:
        current_devices_text += f"""设备名：{i["name"]} | 在线情况：{"在线" if i["is_active"] else "离线"} | 设备类型：{i["type"]} | 是否支持音量调节：{"是" if i["supports_volume"] else "否"} | 当前音量大小：{i["volume_percent"].__str__()}%\n"""
    print(current_devices_text)

    current_devices_text_pure = ""
    for i in current_devices["devices"]:
        if i["is_active"]:
            global playing_volume
            current_devices_text_pure = f"""{"💻" if i["type"] == "Computer" else "📱"}: {i["name"]} ({"在线" if i["is_active"] else "离线"})\n  - 🎚：{"√" if i["supports_volume"] else "X"} \n  - 🔈：{i["volume_percent"].__str__()}%\n"""
            playing_volume = i["volume_percent"]

    current_song_item = spc.current_user_playing_track()["item"]
    song_name = current_song_item["name"]
    song_album_info = current_song_item["album"]
    song_album_name = song_album_info["name"]
    song_album_rdate = song_album_info["release_date"]
    try:
        print(song_album_info["images"])
        song_album_cover = song_album_info["images"][0]["url"]
    except:
        ...

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    song_album_cover_low = song_album_info["images"][2]["url"]
    print(song_album_cover_low)
    with open('cache.png', "wb+") as cf:
        cf.write(requests.get(song_album_cover_low, headers=headers, verify=False).content)
        cf.flush()
        cf.close()

    song_artists_text = ''
    for i in current_song_item["artists"]:
        song_artists_text += f"""      {i["name"]}\n"""
    song_artists_text_pure = ''

    for j in current_song_item["artists"]:
        if len(current_song_item["artists"]) <= 1:
            song_artists_text_pure = j["name"]
        else:
            song_artists_text_pure += f"""{j["name"]}, """
    if len(current_song_item["artists"]) > 1:
        song_artists_text_pure = song_artists_text_pure[:-2]

    print(f"""欢迎，
    当前登录账号显示名：{current_username}
    当前登录设备：{current_devices_text}

    当前播放列表
    正在播放：{song_name}
    所属专辑：{song_album_name} | {song_album_rdate}
    所属专辑封面：{song_album_cover}
    作者：{song_artists_text}
    """)

    pre_message["img_url"] = (song_album_cover)
    pre_message["text"] = {"song_name": song_name, "album_name": song_album_name, "album_rdate": song_album_rdate, "song_artists_pure": song_artists_text_pure, "current_device_pure": current_devices_text_pure}

    show_notification(pre_message)


widgets_btn_show_notification = tk.Button(window, text="Show Notification", command=lambda: processnow())
widgets_btn_show_notification.pack()

widgets_btn_reauthencator = tk.Button(window, text="Re Authenticator", command=lambda: authentication())
widgets_btn_reauthencator.pack()

widgets_entry_toplevelopacity = tk.Entry(window)
widgets_entry_toplevelopacity.pack()

widgets_btn_toplevelopacity = tk.Button(window, text="Process Opacity", command=lambda: process_toplevel_opacity(widgets_entry_toplevelopacity))
widgets_btn_toplevelopacity.pack()

# images = load_tkimage_from_url("http://localhost:8898/b.jpg")
# lb = tk.Label(window, image=images)
# lb.pack()
# print(images)

window.mainloop()
