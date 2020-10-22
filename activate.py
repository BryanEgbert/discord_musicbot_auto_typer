import pyautogui
import subprocess
import click
import time
import sys
import os


@click.command()
@click.option('--prefix', type=str, required=True, help='type your bot command prefix')
@click.option('--vc', type=int, required=True, help='Choose which voice channel to connect')
def main(prefix, vc):
    global runtime
    """This function open the file in read mode if it exist. If the file not exist, create the file"""
    try:
        with open('list.txt', 'r', encoding="cp437", errors="ignore") as file:
            # Read the file content and split it into list
            content = file.read()
            splitted_content = content.split('\n')

            # Open discord app
            subprocess.Popen(os.environ[r"DISCORD_PATH"])

            # Locate the server logo and click it
            logo_location = pyautogui.locateCenterOnScreen(
                ".\\images\\server_logo1.png")

            # Locate voice channel and click it
            voice_channel_location = pyautogui.locateCenterOnScreen(
                f".\\images\\voice_channel{vc}.png")
            pyautogui.click(voice_channel_location)

            # Locate the chatbox and click it
            chatbox_location = pyautogui.locateCenterOnScreen(
                ".\\images\\chatbox.png")
            pyautogui.click(chatbox_location)

            # Looping over the list and write the content.
            # If it done looping all the list, stop the program
            for i in splitted_content:
                if i != '':
                    pyautogui.write(f"{prefix}play {i}", interval=0.03)
                    pyautogui.press('enter')
                    time.sleep(0.02)
                else:
                    continue
            else:
                pyautogui.write(f"{prefix}loop queue")
                pyautogui.press('enter')
                click.echo(f'done!')
                sys.exit()

    except FileNotFoundError:
        click.echo("File not found. Create file. Creating 'list.txt'...")
        with open('list.txt', 'w') as file:
            click.echo('done!')


if __name__ == '__main__':
    main()
