<div id="top"></div>
<p align="center">
  <img src="https://img.shields.io/github/contributors/dropout1337/termfx-reader.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/forks/dropout1337/termfx-reader.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/dropout1337/termfx-reader.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/issues/dropout1337/termfx-reader.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/license/dropout1337/termfx-reader.svg?style=for-the-badge"/>
</p>
  
---------------------------------------
  
<br/>
<div align="center">
  <a href="https://github.com/dropout1337/termfx-reader">
    <img src="https://cdn0.iconfinder.com/data/icons/development-2/24/terminal-512.png" alt="Logo" width="120" height="120">
  </a>
  
  <h2 align="center">Termfx Reader</h3>

  <p align="center">
    Ever wanted to define a variable or a function in a string?
    <br />
    <br />
    <a href="https://github.com/dropout1337/termfx-reader/issues">Report Bug</a>
    ·
    <a href="https://github.com/dropout1337/termfx-reader/issues">Request Feature</a>
  </p>
</div>
  
---------------------------------------

### Features
* Reads functions with multiple arguments
* Reads str/int variables

---------------------------------------

### Installation
* `pip install -U git+https://github.com/dropout1337/termfx-reader`

---------------------------------------

### Usage
```py
import termfx

registry = termfx.New()
registry.register_variable("username", "root")

registry.execute("hello <<$username>>")
```

---------------------------------------

### Creators
* [Dropout](https://t.me/dropoutuwu)<br>
* [Null](https://t.me/epiknull) (Helped with a lot of the function parsing.)<br>
