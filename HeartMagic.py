import subprocess
import json
import pickle
from time import sleep
import textwrap
import os
import sys
from textwrap import wrap
from random import randint, choice

try:
    import pyrogram
finally:
    pass
mod_inst = subprocess.Popen('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pyrogram==1.4.16', True, **('shell',))
mod_inst.wait()
import pyrogram
print(' \n Pyrogram версии 1.4.16 установлен!\n')

try:
    import asyncio
finally:
    pass
mod_inst = subprocess.Popen('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org asyncio', True, **('shell',))
mod_inst.wait()
import asyncio
print(' \n Asyncio установлен!\n')

try:
    import wheel
finally:
    pass
mod_inst = subprocess.Popen('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org wheel', True, **('shell',))
mod_inst.wait()
import wheel
print(' \n Wheel установлен!\n')

try:
    import colorama
finally:
    pass
mod_inst = subprocess.Popen('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org colorama', True, **('shell',))
mod_inst.wait()
import colorama
print(' \n Wheel установлен!\n')

try:
    import requests
finally:
    pass
mod_inst = subprocess.Popen('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests', True, **('shell',))
mod_inst.wait()
import requests
print(' \n Requests установлен!\n')

try:
    import tgcrypto
finally:
    pass
mod_inst = subprocess.Popen('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org tgcrypto==1.2.3', True, **('shell',))
mod_inst.wait()
import tgcrypto
print(' \n TgCrypto установлен!\n')
import random
import json
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from requests import get
from io import BytesIO
import colorama
from colorama import Fore, Back
nex_id = 986023905
drax_id = 994434215
crab_id = 0x1300D31FCL
just_id = 831781432
support_id = 919644121
version = '1.4 '
tag = 'от @asirehsayheart'
tager = 'от @asirehsayheart'
a = [
    'Разработчик',
    'Администратор',
    'DEVELOPER']

def format_exc(e = None, hint = None):
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        if not e.ID:
            pass
        return f'''<b>Telegram API error!</b>\n<code>[{e.CODE} {e.NAME}] - {e.MESSAGE}</code>'''
    if None:
        hint_text = f'''\n\n<b>Hint: {hint}</b>'''
    else:
        hint_text = ''
    return f'''<b>Error!</b>\n<code>{e.__class__.__name__}: {e}</code>''' + hint_text


def with_reply(func):
    
    async def wrapped(client = None, message = None):
        if not message.reply_to_message:
            await message.edit('<b>Reply to message is required</b>')
        else:
            await func(client, message)
            return <NODE:27>

    return wrapped

if os.sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')






print(Fore.RED + f'''\n Пользуясь ботом вы автоматически принимаете и соглашаетесь со\n всеми правилами пользовательского соглашения. \n\n{Fore.LIGHTYELLOW_EX} ''')
sleep(3)
m = '\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x88'
h = '\xe2\x95\x94\xe2\x94\x93\xe2\x94\x8f\xe2\x95\xa6\xe2\x94\x81\xe2\x94\x81\xe2\x95\xa6\xe2\x94\x93\xe2\x95\x94\xe2\x94\x93\xe2\x95\x94\xe2\x94\x81\xe2\x94\x81\xe2\x95\x97 \n\xe2\x95\x91\xe2\x94\x97\xe2\x94\x9b\xe2\x95\x91\xe2\x94\x97\xe2\x94\x81\xe2\x95\xa3\xe2\x94\x83\xe2\x95\x91\xe2\x94\x83\xe2\x95\x91\xe2\x95\xaf\xe2\x95\xb0\xe2\x95\x91 \n\xe2\x95\x91\xe2\x94\x8f\xe2\x94\x93\xe2\x95\x91\xe2\x94\x8f\xe2\x94\x81\xe2\x95\xa3\xe2\x94\x97\xe2\x95\xa3\xe2\x94\x97\xe2\x95\xa3\xe2\x95\xb0\xe2\x95\xaf\xe2\x95\x91 \n\xe2\x95\x9a\xe2\x94\x9b\xe2\x94\x97\xe2\x95\xa9\xe2\x94\x81\xe2\x94\x81\xe2\x95\xa9\xe2\x94\x81\xe2\x95\xa9\xe2\x94\x81\xe2\x95\xa9\xe2\x94\x81\xe2\x94\x81\xe2\x95\x9d'
fuckk = '\n\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\n\xe2\x96\x8f\xe2\x95\xb0\xe2\x94\x88\xe2\x95\xae\xe2\x94\x88\xe2\x95\xb2\xe2\x95\xb2\xe2\x94\x88\xe2\x95\xb1\xe2\x95\xb1\xe2\x94\x88\xe2\x95\xad\xe2\x94\x88\xe2\x95\xaf\xe2\x96\x95\n\xe2\x95\xb2\xe2\x95\xae\xe2\x94\x88\xe2\x95\xb0\xe2\x94\x88\xe2\x95\xae\xe2\x95\xb2\xe2\x96\x89\xe2\x95\xb1\xe2\x95\xad\xe2\x94\x88\xe2\x95\xaf\xe2\x94\x88\xe2\x95\xad\xe2\x95\xb1\n\xe2\x96\x95\xe2\x95\xb0\xe2\x94\x88\xe2\x95\xae\xe2\x94\x88\xe2\x95\xb0\xe2\x95\xae\xe2\x96\x89\xe2\x95\xad\xe2\x95\xaf\xe2\x94\x88\xe2\x95\xad\xe2\x94\x88\xe2\x95\xaf\xe2\x96\x8f\n\xe2\x94\x88\xe2\x95\xb2\xe2\x96\x82\xe2\x95\xb0\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x89\xe2\x95\xb2\xe2\x94\x88\xe2\x94\x88\xe2\x95\xaf\xe2\x96\x82\xe2\x95\xb1\n\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xad\xe2\x96\x8a\xe2\x95\xae\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\n\xe2\x94\x88\xe2\x94\x88\xe2\x96\x8f\xe2\x95\xad\xe2\x94\x88\xe2\x94\x88\xe2\x95\xaf\xe2\x96\x8a\xe2\x95\xb0\xe2\x94\x88\xe2\x94\x88\xe2\x95\xae\xe2\x96\x95\n\xe2\x94\x88\xe2\x96\x95\xe2\x95\xad\xe2\x95\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x8b\xe2\x95\xb2\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb0\xe2\x95\xae\xe2\x96\x8f\n\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\n'
d = ' \n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x95\x97\n\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x95\x91\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d'
app = Client('starzed', 'ru', 15897262, '90476d9c65a86b03837e1e249314cd75', **('lang_code', 'api_id', 'api_hash'))
app.start()
app.stop()
if os.sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')
sleep(1)
print(Fore.LIGHTCYAN_EX + f''' \n\n ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤ ││┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX} \n {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.4 ┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: asirehsayheart┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}\n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}\n {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------\n \n\n''')
sleep(0.05)
if os.sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')
print(Fore.LIGHTCYAN_EX + f''' \n\n ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤ ││┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX} \n {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.4 ┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: asirehsayheart┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}\n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}\n {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------\n \n\n''')
sleep(0.05)
if os.sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')
print(Fore.LIGHTCYAN_EX + f''' \n\n ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤ ││┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX} \n {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.4 ┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: asirehsayheart┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}\n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}\n {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------\n \n\n''')
sleep(0.05)
if os.sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')
print(Fore.LIGHTCYAN_EX + f''' \n\n ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤ ││┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX} \n {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.4 ┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: asirehsayheart┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}\n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}\n {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------\n \n\n''')
sleep(0.05)
if os.sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')
print(Fore.LIGHTCYAN_EX + f''' \n\n ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}\n ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤ ││┃█{Fore.LIGHTCYAN_EX}\n {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX} \n {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.4 ┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: asirehsayheart┃█{Fore.LIGHTCYAN_EX} \n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}\n {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}\n {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------\n \n\n''')
sleep(0.05)
if os.sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')
print(Fore.LIGHTYELLOW_EX + f''' \n\n ---{Fore.LIGHTYELLOW_EX}███{Fore.YELLOW}██████████████████████{Fore.LIGHTYELLOW_EX}\n ---{Fore.LIGHTYELLOW_EX}█{Fore.LIGHTYELLOW_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTYELLOW_EX}\n ---{Fore.LIGHTYELLOW_EX}█{Fore.LIGHTYELLOW_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTYELLOW_EX}\n {Fore.LIGHTYELLOW_EX} ████{Fore.LIGHTYELLOW_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤ ││┃█{Fore.LIGHTYELLOW_EX}\n {Fore.LIGHTYELLOW_EX} █{Fore.LIGHTYELLOW_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTYELLOW_EX} \n {Fore.LIGHTYELLOW_EX}█{Fore.LIGHTYELLOW_EX}┊Version: 1.4 ┃█{Fore.LIGHTYELLOW_EX} \n {Fore.YELLOW}█{Fore.LIGHTYELLOW_EX}┊Telegram: asirehsayheart┃█{Fore.LIGHTYELLOW_EX} \n {Fore.YELLOW} █{Fore.LIGHTYELLOW_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTYELLOW_EX}\n {Fore.YELLOW} █{Fore.LIGHTYELLOW_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTYELLOW_EX}\n {Fore.YELLOW}██████████████████{Fore.LIGHTYELLOW_EX}█---------\n \n''')
print(Fore.LIGHTYELLOW_EX + f'''\n ► {Fore.YELLOW}МЫ {Fore.LIGHTYELLOW_EX}НЕ{Fore.YELLOW} Н{Fore.LIGHTYELLOW_EX}ЕС{Fore.YELLOW}ЕМ{Fore.LIGHTYELLOW_EX} О{Fore.YELLOW}ТВ{Fore.LIGHTYELLOW_EX}ЕТ{Fore.YELLOW}СВ{Fore.LIGHTYELLOW_EX}ЕН{Fore.YELLOW}НО{Fore.LIGHTYELLOW_EX}СТ{Fore.YELLOW}И З{Fore.LIGHTYELLOW_EX}А ВА{Fore.YELLOW}ШИ ДЕ{Fore.LIGHTYELLOW_EX}ЙС{Fore.YELLOW}ТВ{Fore.LIGHTYELLOW_EX}ИЯ! ◄ ''')
print()
number = 0
cool = 3