import pyautogui
import subprocess
import click
import time
import sys
import os

@click.command()
@click.option('--prefix',type=str ,required=True, help='type your bot command prefix')
@click.option('--vc', type=int, required=True, help='Choose which voice channel to connect')
def main(prefix, vc):
    try:
        """This function open the file in read mode if it exist. If the file not exist, create the file"""
        with open('list.txt', 'r', encoding="cp437", errors="ignore") as file:
            # Read the file content and split it into list
            content = file.read()
            splitted_content = content.split('\n')
            
            # Open discord app
            subprocess.Popen(os.environ[r"DISCORD_PATH"])

            # Locate the server logo and click it
            logo_location = pyautogui.locateCenterOnScreen(r".\images\server_logo1.png")
            pyautogui.click(logo_location)

            # Locate voice channel and click it
            voice_channel_location = pyautogui.locateCenterOnScreen(f".\\images\\voice_channel{vc}.png")
            pyautogui.click(voice_channel_location)

            # Locate the chatbox and click it
            chatbox_location = pyautogui.locateCenterOnScreen(r".\images\chatbox.png")
            pyautogui.click(chatbox_location)

            # Looping over the list and write the content.
            # If it done looping all the list, stop the program
            for i in splitted_content:
                if i != '':
                    pyautogui.write(f"{prefix}play {i}", interval=0.01)
                    pyautogui.press('enter')
                else:
                    continue
            else:
                time.sleep(1)
                pyautogui.write(f"{prefix}loop queue")
                pyautogui.press('enter')
                click.echo('done!')
                sys.exit()

    except FileNotFoundError:
        with open('list.txt', 'w') as file:
            pass

if __name__ == '__main__':
    main()