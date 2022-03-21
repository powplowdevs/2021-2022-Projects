import pyppeteer
import asyncio
import pyautogui as pa
import pyperclip 
import time

async def main():
    # launches a chromium browser, can use chrome instead of chromium as well.
    browser = await pyppeteer.launch(headless=False)
    # creates a blank page
    page = await browser.newPage()
    # follows to the requested page and runs the dynamic code on the site.
    await page.goto('https://crypto.com/nft/')
    time.sleep(4)
    
    #use inspect to get html
    #hit root not the body
    pa.keyDown("ctrl")
    pa.keyDown("shift")
    pa.keyDown("i")
    time.sleep(0.5)
    pa.keyUp("ctrl")
    pa.keyUp("shift")
    pa.keyUp("i")
    time.sleep(0.5)
    pa.moveTo(800,220)
    time.sleep(0.5)
    pa.click(button="right")
    time.sleep(0.5)
    pa.moveTo(900,310)
    time.sleep(0.5)
    pa.moveTo(970,400)
    time.sleep(0.5)
    pa.click(button="left")
    time.sleep(0.5)
    # pa.click(button="left")
    # time.sleep(0.5)
    # pa.keyDown("ctrl")
    # pa.keyDown("a")
    # time.sleep(0.5)
    # pa.keyUp("ctrl")
    # pa.keyUp("a")   
    # time.sleep(0.5)
    # pa.keyDown("ctrl")
    # pa.keyDown("c")
    # time.sleep(0.5)
    # pa.keyUp("ctrl")
    # pa.keyUp("c") 
    # time.sleep(0.5)
    cont = pyperclip.paste()
    time.sleep(100000)

    return cont

# prints the html code of the user profiel: tupac
print(asyncio.get_event_loop().run_until_complete(main()))