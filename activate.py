import pyautogui
import subprocess
import shutil
import click
import time
import sys
import cv2
import os

# Image directory
vc_image_dir = ".\\images\\voice_channel"
server_image_dir = ".\\images\\server_img"
chat_image_dir = ".\\images\\chat_channel"

# File inside the image directory
server_img = os.listdir(server_image_dir)
vc_img = os.listdir(vc_image_dir)
chat_img = os.listdir(chat_image_dir)


@click.group()
def cli():
    pass


@cli.command()
@click.option('-p', '--prefix', type=str, required=True, help='type your bot command prefix')
@click.option('-vc', type=int, default=1, show_default=True, help='Choose which voice channel to connect.')
@click.option('-c', '--chat', type=int, default=1, show_default=True, help='Choose which chat to click.')
@click.option('-s', '--server', type=int, default=1, show_default=True, help='Choose which server logo to click.')
def main(prefix, vc, chat, server):
    """The main function"""
    try:
        """Validate if the file in image directory exist of not"""

        # Checking the file in .\images\server_img directory
        os.path.isfile(
            f"{server_image_dir}\\{server_img[server-1]}")

        # Checking file in .\images\voice_channel directory
        os.path.isfile(
            f"{vc_image_dir}\\{vc_img[vc-1]}")

        # Checking file in .\images\chat_channel directory
        os.path.isfile(
            f"{chat_image_dir}\\{chat_img[chat-1]}")

        # Checking the chatbox image
        os.path.isfile(
            ".\\images\\chatbox.png")

    except FileNotFoundError:
        click.echo("File not found. Create file. Creating 'list.txt'...")
        with open('list.txt', 'w') as file:
            click.echo('done!')

    except IndexError:
        click.secho('ERROR: Image file not available. Use the view command to see the file available or --help command to see available commands', fg='bright_red')
    else:
        try:
            # Open discord app
            subprocess.Popen(os.environ["DISCORD_PATH"])
            time.sleep(2)
            logo_location = pyautogui.locateCenterOnScreen(
                f"{server_image_dir}\\{server_img[server-1]}", confidence=0.6)
            pyautogui.click(logo_location)
            time.sleep(1)

            # Locate voice channel and click it
            voice_channel_location = pyautogui.locateCenterOnScreen(
                f"{vc_image_dir}\\{vc_img[vc-1]}", confidence=0.8)
            pyautogui.click(voice_channel_location, clicks=1)
            time.sleep(1)

            # Locate chat channel and click it
            chat_channel_location = pyautogui.locateCenterOnScreen(
                f"{chat_image_dir}\\{chat_img[chat-1]}", confidence=0.7)
            pyautogui.click(chat_channel_location)

            # Locate the chatbox and click it
            chatbox_location = pyautogui.locateCenterOnScreen(
                ".\\images\\chatbox.png", confidence=0.3)
            pyautogui.click(chatbox_location)

            with open('list.txt', 'r', encoding="cp437", errors="ignore") as file:
                # Read the file content and split it into list
                content = file.read()
                splitted_content = content.split('\n')
                # Looping over the list and write the content.
                # If it done looping all the list, stop the program
                for i in splitted_content:
                    # Check for empty string e.g.line break 
                    if i != '':
                        pyautogui.write(f"{prefix}play {i}", interval=0.03)
                        pyautogui.press('enter')
                        time.sleep(0.02)
                    # If exist, skip it and continue the loop
                    else:
                        continue
                else:
                    # Enter loop queue command.
                    # If the command prefix is "-"(Groovy musicbot)
                    if (prefix == "-"):
                        pyautogui.write(f"{prefix}loop queue")
                    # If the command prefix is "!"(Rythm musicbot)
                    else:
                        pyautogui.write(f"{prefix}loopqueue")
                    pyautogui.press('enter')
                    click.secho('done!', fg='green')
                    sys.exit()
        except pyautogui.FailSafeException:
            click.secho('Execution has been stopped', fg='yellow')


@cli.command()
@click.argument("image")
def add_vc(image):
    """Add voice channel image"""
    if n == None and image.endswith((".jpg", ".png", ".jpeg")):
        shutil.copy(src=image, dst=vc_image_dir)
    elif n != None and image.endswith((".jpg", ".png", ".jpeg")) and n.endswith((".jpg", ".png", ".jpeg")):
        shutil.copyfile(src=image, dst=f"{vc_image_dir}\\{n}")
    else:
        click.echo(
            "FILE TYPE ERROR: Please put the file type e.g.filename.png or invalid image file type", fg='bright_red')


@cli.command()
@click.argument("image")
@click.option("-n", help="Rename file")
def add_logo(image, n):
    """Add server logo image"""
    if (n == None and image.endswith((".jpg", ".png", ".jpeg"))):
        shutil.copy(src=image, dst=server_image_dir)
    elif (n != None and image.endswith((".jpg", ".png", ".jpeg")) and n.endswith((".jpg", ".png", ".jpeg"))):
        shutil.copyfile(src=image, dst=f"{server_image_dir}\\{n}")
    else:
        click.secho(
            "FILE TYPE ERROR: Please put the file type e.g.filename.png or invalid image file type", fg='bright_red')


@cli.command()
@click.argument("image")
@click.option("-n", help="Rename file")
def add_channel(image, n):
    """Add chat channel image"""
    if (n == None and image.endswith((".jpg", ".png", ".jpeg"))):
        shutil.copy(src=image, dst=chat_image_dir)
    elif (n != None and image.endswith((".jpg", ".png", ".jpeg")) and n.endswith((".jpg", ".png", ".jpeg"))):
        shutil.copyfile(src=image, dst=f"{chat_image_dir}\\{n}")
    else:
        click.echo(
            "FILE TYPE ERROR: Please put the file type e.g. filename.png or invalid image file type", fg='bright_red')


@cli.command()
def view():
    """View list images"""
    click.secho("\nVoice Channel", fg='cyan', bold=True, underline=True)
    if len(os.listdir(vc_image_dir)) != 0:
        for i in os.listdir(vc_image_dir):
            click.secho("  -" + i, fg='green')
    else:
        click.secho("  -none", fg='red')

    click.secho("\nServer", fg='cyan', bold=True, underline=True)
    if len(os.listdir(server_image_dir)) != 0:
        for i in os.listdir(server_image_dir):
            click.secho("  -" + i, fg='green')
    else:
        click.secho("  -none", fg='red')

    click.secho("\nChat Channel", fg='cyan', bold=True, underline=True)
    if (len(os.listdir(chat_image_dir)) != 0):
        for i in os.listdir(chat_image_dir):
            click.secho("  -" + i, fg='green')
        else:
            click.echo("")
    else:
        click.secho("  -none\n", fg='red')


if __name__ == '__main__':
    cli()
