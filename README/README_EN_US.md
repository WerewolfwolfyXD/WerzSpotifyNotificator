<br />
<p align="center">
  	<h2 align="center" style="font-size:50px">Werz<br><font color="green">Spotify</font>Notificator</h2>
  	<h2 align="center" style="font-size:10px;">WerzSpotifyNotificator | Powered by Spotify, Spotipy
  	<p align="center" style="font-size:20px">
    		An inexplicable <font color="green">Spotify</font> Notificator
    <br />
	<div class="nextline" style="font-size:15px;"><a href="https://github.com/WerewolfwolfyXD/WerzSpotifyNotificator/release">📦Release</a> | <a href="https://github.com/WerewolfwolfyXD/WerzSpotifyNotificator/blob/main/README.md">🌎Main Page</a></div>
    <br />
    <br />
  </p>
</p>

<tr>
<!-- Preview Part -->

###### Other README:
[English](README/README_EN_US.md)

# <left><a>📷<a style="font-size:15px;">⭐ Preview | Screenshots</a></left>

<img src="/README/materials/0.png" alt="Bear-Z - Red & White (Pt.II) Notification" width="400" />
<img src="/README/materials/1.png" alt="CarbondoXD - Fantasy Notification" width=400" />
<br>
<img src="/README/materials/2.png" alt="Bear-Z - Red & White (Pt.II) Desktoply" width="945" /><br>
<img src="/README/materials/3.png" alt="CarbondoXD - Fantasy Desktoply" width="945" /><br>

<!-- TODO PART -->
# <left><a>✔<a style="font-size:18px">TODO</a>
Now in [Projects](https://github.com/WerewolfwolfyXD/WerzSpotifyNotificator/projects)

<!-- Description Part -->
# <left>📕<a style="font-size:18px;">Introduction</a></left>
#### WerzSpotifyNotificator is a current playtrack messager tools based in Spotify Developer Web API, My code is bad, if you'd like to edit, just do it.
#### <h6>Debug Environment: Windows Subsystem Linux 2 (kali-linux) in Windows 11 22H2</h6>

<!-- Build Part -->
# <left>⚙<a style="font-size:18px;">Start Building</a></left>
##### Before we start, we gonna use： [`Python3 (3.11 or 3.10 are tested)`]() 
- [x] Python3 `WIP`
- [ ] Rust `Projecting WIP`

⚠ Before building：Make sure you are using different venv and which you'd like to use as the main interpreter (`Anaconda`, `Python Venv`)

`I'm sorry for that I have no devices installed MacOS；Configuration in MacOS could see Linux/GNU`

<!-- StartBuild - Python3 -->
# <left><a>🔧<a style="font-size:15px;">⭐ Start Building::Python3</a></left>
###### Make sure your current path in ./src!

## 💻(Windows Script | *.bat, *.cmd)
```shell
# For Anaconda
conda create --name <Venv name> python=3.10 && conda activate && python -m pip install -r requirements.txt

# For Python Venv🐍
set _ENVN=<Venv name> && python3 -m venv %_ENVN% && cd %ENVN%\Scripts\activate && pip install -r requirements.txt
```


## 🐧(Linux/GNU Script | *.sh)
```shell
# For Anaconda
sudo conda create --name <Venv name> python=3.10 && conda activate && python -m pip install -r requirements.txt

# For Python Venv🐍
export _ENVN=<Venv name> && python3 -m venv $_ENVN && cd $ENVN/Scripts/activate && pip install -r requirements.txt
```

<!-- StartRun - Python3 -->
# <left><a>🔧<a style="font-size:15px;">⭐ Start Running::Python3</a></left>
###### Make sure your current path is ./src

## 💻(Windows Script | *.bat, *.cmd)
```shell
# Command Prompt - 1
# Working in Virtual Environment
python FlaskServer.py


# Command Prompt - 2
# Working in Virtual Environment
# [Running for the first time]
python main.py
# If your browser return to localhost then the interpreter was freeze,
# Kill the command prompt, and run python main.py again
# [Running for the second time]
python main.py
# After run the second time, you needn't to run 2 times again!
# Then, here's a window of the main program, enjoy it!
```


## 🐧(Linux/GNU Script | *.sh)
```shell
# Bash Terminal - 1
# Working in Virtual Environment
python FlaskServer.py


# Bash Terminal - 2
# Working in Virtual Environment
# [Running for the first time]
python main.py
# If your browser return to localhost then the interpreter was freeze,
# Kill the command prompt, and run python main.py again
# [Running for the second time]
python main.py
# After run the second time, you needn't to run 2 times again!
# Then, here's a window of the main program, enjoy it!
```