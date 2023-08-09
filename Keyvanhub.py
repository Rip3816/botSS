import os as os
from bs4 import *
import requests as requests
from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram import Client, filters
import pyromod.listen
from time import sleep
import re
bot = Client(

name = "tkbot",

api_id = 2717155,

api_hash = "4f8329cb2062f68735701675aedc39ed",

bot_token = "6341318463:AAHo6Dh0F9UQH2Ht3js5ljizYIsyKXqmeL4"

)

os.chdir("\\")
@bot.on_message(filters.command('start'))
async def Hello(client,message):
     chat_id = message.chat.id
     await client.send_message(chat_id,f'Hello \nyour user id: @{message.chat.username}')

         
@bot.on_message(filters.command('xd'))
async def xvideo(client,message):
     link = await message.chat.ask('get me your video link: ')
     regex = r"\d{8}"
     extract = re.search(regex,link.text)
     post_id = extract.group()
     url = f"https://www.xvideos.com/video-download/{post_id}/"
     response = requests.get(url)
     headers = {'Cookie':'html5_pref={"SQ":false,"MUTE":false,"VOLUME":1,"FORCENOPICTURE":false,"FORCENOAUTOBUFFER":false,"FORCENATIVEHLS":false,"PLAUTOPLAY":true,"CHROMECAST":false,"EXPANDED":false,"FORCENOLOOP":false}; disclaimer_vpn_display=OK; wpn_ad_cookie=72c7c00e1f2ae58c1c0351c14bbe95ca; session_ath=light; html5_networkspeed=11108; last_subs_check=1; last_views=["59161635-1689259249","40075011-1691342835","77130603-1691407793","76629573-1691415086","75070621-1691415672"]; session_token=7aa40e9b2fda10cfDZ305XB5RTcoMph6vk5NkdKyfKpXO9KI-RlLUgQKRKa9sQHvS1WoOAxibmeWJMkgRBEiwgc5Ru1BnXt0Gs1zPihh7IVXGk7ElkkVR9taOvcP3SxW1mAWcEkCuf8uwmL8-aIiiITFBUYo_RUXket8mHXxOwUGbbosDcn47Wg_8dA3YFGsbTcfKtJwU79QsbHRMeV1P10ewgPCoGmNvqvNnjBrObnJtb8o0DVV94eNYmgUHZGO8qFBUMvd475nnwtlO3bAia9os8abFyqV1EeOFJ-Nc42MlXqFKUXEpF9b2TQPl471_ZNDVYTjFhjJJAXykE4_guNFbfV9wPM_5BSxY7UdWhbXJbVZMrYmXLFoN9fXIruuPiaIPpPwil6auHpslXdEB2C0EWyZRTHDVZj86G_gpXlIZgGhaU0EuUXKIHHdZC-wxTxbG-z1K3FXFHl5Yr-FbmHTNKkpNGdsdY1U9BTLeV_PulNdO2sBoDT_NfrS_91tW4I3ZizyePhQV-WA'}
     send = requests.post(url = url,headers = headers)
     result = send.json()
     Best_Quality = result['URL']
     remove = Best_Quality.removesuffix('?download=1')
     video = remove
     r = requests.get(video)
     file = await message.chat.ask('get me a name: : ')
     open(file.text+'.mp4', 'wb').write(r.content)
     l = os.listdir('.')
     print (l)
     if f'{file.text}.mp4' in l:
           main = await bot.send_video(message.chat.id, f"{file.text}.mp4")
           sleep(10)
           await bot.delete_messages(message.chat_id, main.id)
     else:
           await bot.send_message(message.chat.id,'A problem')       
     
@bot.on_message(filters.command('xnxx'))
async def xnxx (client,message):
     link = await message.chat.ask('get me your video link: ')
     response = requests.get(url = link.text)
     res = re.findall(r'\d{8,}',response.text)
     post_id = res.pop()
     url2 = f'https://www.xnxx.com/video-download/{post_id}/'
     headers = {'Cookie':'wpn_ad_cookie=cb69ce75a8879978fc0344d806bc395a; html5_pref={"SQ":false,"MUTE":false,"VOLUME":1,"FORCENOPICTURE":false,"FORCENOAUTOBUFFER":false,"FORCENATIVEHLS":false,"PLAUTOPLAY":true,"CHROMECAST":false,"EXPANDED":false,"FORCENOLOOP":false}; html5_networkspeed=5408; session_blih=3747cc14ff48cd97w7wOOFVffCOWskAJGem3PHaAMYdEE3oB5AAZsL7NP6U=; last_views=["26920655-1691440916","54892701-1691444719","48556937-1691444895","54044047-1691444897","77473775-1691444997","77444687-1691590973"]; session_token=cc247f77180afa1acT7dETiJtFgEayWJb6XA7zUYOfuFghP57X4c_GKHiKT5y01FAGnjX8beWufgCADAd7LogorhDb68Tpg27aoq8BmTj9trOtmIeoWhCuC_g9Rz8unCg1bW04vdgirWMEdQY5DoUVFa9pNnbmd4EJUXHPNHux-l5en1C6x0QFArtnDjiBInHFXCWglLZtH8xfRF_O7VpadFgUFxyhraYVPiDDs4lnpM0rfGhLUkyIZGHZ_seffoeJfuerwitne8jCLM_xoxrKMeIrkfqvTv6LsNX8jOYVIj-P8PKSzBsnkt60M162gvbmm7XNaQWDmu1yKo4CHJDEdMsFQDlAQxZy0CZMuZyF5haAEzrkBP_VBQpcoFs8fO3Mxsl6trTGc_9q9vbT1xSPGFmYwOom_7lT7BvuGkq9vHDB0CBH0Htm0a01z_6D3bLP5kmGeETqyn_KXT','User-Agent':'Mozilla/5.0 (Linux; Android 12; 2201117PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Referer':link.text,'Host':'www.xnxx.com','Content-Type':'application/json'}
     send = requests.post(url = url2,headers = headers)
     javab = send.json()
     Best = javab['URL']
     cut = Best.removesuffix('?download=1')
     video = cut
     r = requests.get(video)
     file = await message.chat.ask('get me a name: : ')
     open(file.text+'.mp4', 'wb').write(r.content)
     l = os.listdir('.')
     if f'{file.text}.mp4' in l:
          main = await bot.send_video(message.chat.id, f"{file.text}.mp4")
          sleep(10)
          await bot.delete_message(message.chat.id, main.id)
          
     else:
            await bot.send_message(message.chat.id,' A pronlem')
     
     
bot.run()
