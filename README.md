<p align="left">
  <img align="left" height="200" src="https://img.fastmirror.net/s/2024/08/30/66d1b8c5a3519.png" alt="Potato-logo" style="float: left; border-radius: 10px;"/>
</p>

# Potato

一个简洁全能的 Minecraft 服务器检测系统

<div>
    <a href="https://github.com/MCSLTeam/MCSL2/stargazers">
        <img src="https://img.shields.io/github/stars/MCSLTeam/MCSL2?style=for-the-badge" alt="Star">
    </a>
    <a href="https://github.com/MCSLTeam/MCSL2/forks">
        <img src="https://img.shields.io/github/forks/MCSLTeam/MCSL2?style=for-the-badge" alt="Fork">
    </a>
    <a href="https://github.com/MCSLTeam/MCSL2/issues">
        <img src="https://img.shields.io/github/issues/MCSLTeam/MCSL2?style=for-the-badge" alt="Issues">
    </a>
    <br>
    <a href="https://github.com/MCSLTeam/MCSL2/releases">
        <img src="https://img.shields.io/github/downloads/MCSLTeam/MCSL2/total?style=for-the-badge" alt="Downloads">
    </a>
    <a href="https://github.com/MCSLTeam/MCSL2/releases/latest">
        <img src="https://img.shields.io/github/v/tag/MCSLTeam/MCSL2?label=ver&style=for-the-badge" alt="Version">
    </a>
    <a href="mailto:services@mcsl.com.cn">
        <img src="https://img.shields.io/badge/%20CONTACT-services%40mcsl.com.cn-%2357728B?style=for-the-badge" alt="Email">
    </a>
</div>

___

## 他能干什么？  
 
- **💻界面简洁易懂**： 以终端为基础，提供简洁、易懂的界面。  
- **✅准确检测服务器状态**： 配置服务器IP及端口，快速检测  
- **🎞️低资源占用**： 不断优化，持续进步    

## 从源码构建打包版

- `git clone https://github.com/MCSLTeam/MCSL2.git`
- `pip install tomli`
- `python Tools/gen-requirements.py`
- `python -m pip install -U -r requirements.txt`
- `python Tools/update-pyproject.py`
- `python -m lndl_nuitka .`
  - 或者
  - `python -m lndl_nuitka . -y`
  - 又或者通过 `-- --xxx` 添加 / 修改参数
  - `python -m lndl_nuitka . -- --disable-console`

## 相关链接

MCSL 2 官网: <https://mcsl.com.cn>  
GitHub Issue: <https://github.com/MCSLTeam/MCSL2/issues>  
QQ 官方群聊: <https://mcsl.com.cn/links/mcsl2-qq-group.html>  
GPLv3 开源协议: <https://github.com/MCSLTeam/MCSL2/blob/master/LICENSE>  
QFluentWidgets: <https://qfluentwidgets.com>

## 鸣谢

请前往<https://mcsl.com.cn/>查看相关链接。

还有所有的贡献者们！  

<a href="https://github.com/MCSLTeam/MCSL2/graphs/contributors"><img src="https://contrib.rocks/image?repo=MCSLTeam/MCSL2&anon=1&max=100000000"></a>

还有，赞助者们！  
[赞助者列表](https://github.com/MCSLTeam/MCSL2/blob/master/Sponsors.md)

## 声明

本开源项目完全免费，任何倒卖等行为必究。
