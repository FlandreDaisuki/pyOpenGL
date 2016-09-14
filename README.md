#pyOpenGL
測試作業系統為Linux Mint 18(based on Ubuntu 16.04)

但理論上python3可以跑的平台都可以

##前置
- (**必要**) python3.*
- (**非必要**) pyenv

##步驟
確認 Python 版本
```
$ python -V
Python 3.5.2
```
或
```
$ pyenv versions
  system
* 3.5.2
```

用 `pip` 安裝OpenGL相關函式庫
```
$ pip install --upgrade pip
$ pip install PyOpenGL PyOpenGL_accelerate
```

用 `pip` 安裝其他相關函式庫
```
$ pip install numpy # 數值/矩陣運算
$ pip install pillow # 圖片格式
```

測試
```
$ python 0_env.py
$ python 1_teapot.py
$ python 2_shader.py
```

#常見問題
1. pip: command not found

    若使用 `pyenv` 則套用可使用版本到當下路徑
    ```
    $ pyenv local 3.*
    ```
    若使用系統python則
    ```
    $ sudo apt-get install python3-pip
    ```
2. `python -V` 是 2.* 版

    將上述 `python` 都改成 `python3` ，如：
    ```
    $ python3 -V
    $ python3 0_env.py
    ...
    ```

#參考資料
- [PyOpenGL Installation](http://pyopengl.sourceforge.net/documentation/installation.html)
- [PyOpenGL Documentation](http://pyopengl.sourceforge.net/documentation/index.html)
- [pyenv](https://github.com/yyuu/pyenv)
