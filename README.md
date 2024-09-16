<br />
<p align="center">
  	<h2 align="center" style="font-size:50px">Werz<br><font color="green">Spotify</font>Notificator</h2>
  	<h2 align="center" style="font-size:10px;">WerzSpotifyNotificator | Powered by Spotify, Spotipy
  	<p align="center" style="font-size:20px">
    		一个莫名其妙的<font color="green">Spotify</font> Notificator
    <br />
	<div class="nextline" style="font-size:15px;"><a href="https://github.com/WerewolfwolfyXD/WerzSpotifyNotificator/release">📦️发行</a> | <a href="https://github.com/WerewolfwolfyXD/WerzSpotifyNotificator/blob/main/README.md">🌎主页</a></div>
    <br />
    <br />
  </p>
</p>

<tr>
<!-- Preview Part -->

# <left><a>📷<a style="font-size:15px;">⭐ Preview | Screenshots</a></left>

<img src="/README/materials/0.png" alt="Bear-Z - Red & White (Pt.II)" width="500" />
<img src="/README/materials/1.png" alt="Bear-Z - Red & White (Pt.II)" width=440" />
<br>
<img src="/README/materials/2.png" alt="Bear-Z - Red & White (Pt.II)" width="945" /><br>
<img src="/README/materials/3.png" alt="Bear-Z - Red & White (Pt.II)" width="945" /><br>

<!-- TODO PART -->
# <left><a>✔<a style="font-size:18px">TODO</a>
现在放置于[Projects](https://github.com/WerewolfwolfyXD/WerzSpotifyNotificator/projects)中

<!-- Description Part -->
# <left>📕<a style="font-size:18px;">介绍</a></left>
#### WerzSpotifyNotificator是一个调用Spotify Developer Web API的信息获取器，意于弹出窗口来查看当前Playtrack，主要我的代码就像屎山。我也不太写注释，如果看得懂的话可以尝试看看。
#### <h6>调试环境：Windows Subsystem Linux 2 (kali-linux) in Windows 11 22H2<br>Debug Environment: Windows Subsystem Linux 2 (kali-linux) in Windows 11 22H2</h6>

<!-- Build Part -->
# <left>⚙<a style="font-size:18px;">开始构建</a></left>
##### 在开始使用前，我们需要明确使用的版本： [`Python3 (3.11 or 3.10 are tested)`]() 
- [x] Python3 `WIP`
- [ ] Rust `Projecting WIP`

⚠ 开始构建前：请确保如果你需要在一个新的虚拟环境(`Anaconda`, `Python Venv`)中使用不同的版本

`很抱歉我没有Mac，包括有MacOS的任何设备；Mac的配置可以参考Linux/GNU的。`

<!-- StartBuild - Python3 -->
# <left><a>🔧<a style="font-size:15px;">⭐ 开始构建::Python3</a></left>
###### 您需要确保当前目录位于src中

## 💻(Windows Script | *.bat, *.cmd)
```shell
# For Anaconda
conda create --name <环境名称> python=3.10 && conda activate && python -m pip install -r requirements.txt

# For Python Venv🐍
set _ENVN=<环境名称> && python3 -m venv %_ENVN% && cd %ENVN%\Scripts\activate && pip install -r requirements.txt
```


## 🐧(Linux/GNU Script | *.sh)
```shell
# For Anaconda
sudo conda create --name <环境名称> python=3.10 && conda activate && python -m pip install -r requirements.txt

# For Python Venv🐍
export _ENVN=<环境名称> && python3 -m venv $_ENVN && cd $ENVN/Scripts/activate && pip install -r requirements.txt
```