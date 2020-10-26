import pyautogui
import subprocess
import click
import time
import sys
import os

@click.group()
def cli():
    pass

@cli.command()
@click.option('--prefix', type=str, required=True, help='type your bot command prefix')
@click.option('-vc', type=int, required=True, help='Choose which voice channel to connect')
def main(prefix, vc):
    """The main function"""
    try:
        with open('list.txt', 'r', encoding="cp437", errors="ignore") as file:
            # Read the file content and split it into list
            content = file.read()
            splitted_content = content.split('\n')

            # Open discord app
            subprocess.Popen(os.environ[r"DISCORD_PATH"])

            # Locate the server logo and click it
            logo_location = pyautogui.locateCenterOnScreen(
                ".\\images\\server_img\\server_logo1.png")
            pyautogui.click(logo_location, confidence=0.6)

            # Locate voice channel and click it
            voice_channel_location = pyautogui.locateCenterOnScreen(
                f".\\images\\voice_channel\\voice_channel{vc}.png")
            pyautogui.click(voice_channel_location, confidence=0.6)

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
                if (prefix == "-"):
                    pyautogui.write(f"{prefix}loop queue")
                else:
                    pyautogui.write(f"{prefix}loopqueue")
                pyautogui.press('enter')
                click.echo(f'done!')
                sys.exit()

    except FileNotFoundError:
        click.echo("File not found. Create file. Creating 'list.txt'...")
        with open('list.txt', 'w') as file:
            click.echo('done!')
    
@cli.command()
@click.argument("image")
def add_vc(image):
    """Add voice channel image"""
    pass

@cli.command()
@click.argument("image")
def add_logo(image):
    pass

@cli.command()
@click.argument("image")
def add_channel(image):
    pass

@cli.command()
def view():
    vc_image_dir = ".\\images\\voice_channel"
    click.echo("\nVoice Channel")
    for i in os.listdir(vc_image_dir):
        click.echo("-"+ i)

    server_image_dir = ".\\images\\server_img"
    click.echo("\nServer")
    for i in os.listdir(server_image_dir):
        click.echo("-" + i)


if __name__ == '__main__':
    cli()
