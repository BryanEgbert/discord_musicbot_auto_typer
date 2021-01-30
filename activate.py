import pyautogui
import subprocess
import shutil
import click
import time
import sys
import cv2
import re
import os

# Image directory
current_working_dir = os.path.dirname(os.path.abspath(__file__))
vc_image_dir = f"{current_working_dir}\\dmat\\images\\voice_channel"
server_image_dir = f"{current_working_dir}\\dmat\\images\\server_img"
chat_image_dir = f"{current_working_dir}\\dmat\\images\\chat_channel"

# File inside the image directory
server_img = os.listdir(server_image_dir)
vc_img = os.listdir(vc_image_dir)
chat_img = os.listdir(chat_image_dir)

pyautogui.PAUSE = 0.5

@click.group()
def cli():
    pass


@cli.command()
@click.option('-pre', '--prefix', type=str, required=True, help='type your bot command prefix')
@click.option('-vc', type=int, default=1, show_default=True, help='Choose which voice channel to connect.')
@click.option('-c', '--chat', type=int, default=1, show_default=True, help='Choose which chat to click.')
@click.option('-s', '--server', type=int, default=1, show_default=True, help='Choose which server logo to click.')
@click.option('-play', '--playlist', type=int, required=True, help='Choose what playlist to play')
def main(prefix, vc, chat, server, playlist):
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
            ".\\dmat\\images\\chatbox.png")

    except FileNotFoundError:
        click.secho(
            "ERROR: Playlist is empty. Use register -p[PATH] command to add playlist", fg='bright_red')

    except IndexError:
        click.secho('ERROR: Image file not available. Use the view command to see the file available or --help command to see available commands', fg='bright_red')
    else:
        try:
            # Open discord app
            with open(".\\dmat\\discord_path.txt", "r") as file:
                discord_path = file.read()
                subprocess.Popen(discord_path)
            time.sleep(2.5)

            # Locate server logo location and click it
            logo_location = pyautogui.locateCenterOnScreen(
                f"{server_image_dir}\\{server_img[server-1]}", confidence=0.6)
            pyautogui.click(logo_location)

            # Locate voice channel and click it
            voice_channel_location = pyautogui.locateCenterOnScreen(
                f"{vc_image_dir}\\{vc_img[vc-1]}", confidence=0.8)
            if(voice_channel_location == None):
                # dc_channel = pyautogui.locateCenterOnScreen(
                #     ".\\images\\dc_channel.png", confidence=0.4)
                pyautogui.moveRel(100,100)
                print(voice_channel_location)

                while (voice_channel_location == None):
                    pyautogui.PAUSE=0.2
                    pyautogui.scroll(-120)
                    voice_channel_location = pyautogui.locateCenterOnScreen(
                        f"{vc_image_dir}\\{vc_img[vc-1]}", confidence=0.8)
                else:
                    pyautogui.click(voice_channel_location)
            else:
                pyautogui.click(voice_channel_location)
                pyautogui.PAUSE = 2
            time.sleep(1)

            # Locate chat channel and click it
            chat_channel_location = pyautogui.locateCenterOnScreen(
                f"{chat_image_dir}\\{chat_img[chat-1]}", confidence=0.7)
            while chat_channel_location == None:
                print(chat_channel_location)
                pyautogui.moveRel(0,-300)
                pyautogui.scroll(-50)
                chat_channel_location = pyautogui.locateCenterOnScreen(
                    f"{chat_image_dir}\\{chat_img[chat-1]}", confidence=0.7)
            else:
                pyautogui.click(chat_channel_location)

            # Locate the chatbox and click it
            chatbox_location = pyautogui.locateCenterOnScreen(
                ".\\dmat\\images\\chatbox.png", confidence=0.4)
            pyautogui.click(chatbox_location)

            # Open playlist.txt in read mode
            with open('.\\dmat\\playlist.txt', 'r') as file:
                file_content = file.read()
                stripped_content = file_content.strip(" ")
                playlists = stripped_content.split('\n')
                # Open the textfile path stored inside playlist.txt
                with open(playlists[playlist-1], 'r', encoding="cp437", errors="ignore") as songs:
                    # Read and split the content into list based on line break
                    song_content = songs.read()
                    splitted_content = song_content.split('\n')

                    # Looping over the list and write the content.
                    for i in splitted_content:
                        # Check for empty string e.g.line break
                        if i != '':
                            pyautogui.write(f"{prefix}play {i}", interval=0.03)
                            pyautogui.press('enter')
            
                        # If exist, skip it and continue the loop
                        else:
                            continue
                    # If the loop has completed
                    else:
                        time.sleep(1)
                        if prefix == "-":
                            # Write loop queue command
                            pyautogui.write(
                                f"{prefix}loop queue", interval=0.03)
                        else:
                            pyautogui.write(
                                f"{prefix}loopqueue", interval=0.03)

                        pyautogui.press('enter')
                        click.secho('done!', fg='green')
                        sys.exit()
        except pyautogui.FailSafeException:
            click.secho('Execution has been stopped', fg='yellow')
        except OSError:
            click.secho(
                "ERROR: Discord.exe path couldn't be found or missing. Use register -d[PATH] command to add discord path", fg='bright_red')


class CopyImage:
    """This class validate the file type and copy the file into images subdirectory"""

    def __init__(self, image, name, dir):
        self.image = image
        self.name = name
        self.dir = dir
        # Check if the file ends with .png, .jpg, .jpeg
        if (self.name == None and self.image.endswith((".jpg", ".png", ".jpeg"))):
            shutil.copy(src=image, dst=self.dir)
        elif (self.name != None and self.image.endswith((".jpg", ".png", ".jpeg")) and self.name.endswith((".jpg", ".png", ".jpeg"))):
            shutil.copyfile(src=image, dst=f"{self.dir}\\{self.name}")
        # Give error if the file type is invalid
        else:
            click.secho(
                "FILE TYPE ERROR: Please put the file type e.g.filename.png or invalid image file type", fg='bright_red')


@cli.command()
@click.argument("image", type=click.Path(exists=True))
@click.option("-n", "--name", help="Rename file")
def add_vc(image, name):
    """Add voice channel image"""
    CopyImage(image, name, vc_image_dir)


@cli.command()
@click.argument("image", type=click.Path(exists=True))
@click.option("-n", "--name", help="Rename file")
def add_logo(image, name):
    """Add server logo image"""
    CopyImage(image, name, server_image_dir)


@cli.command()
@click.argument("image", type=click.Path(exists=True))
@click.option("-n", "--name", help="Rename file")
def add_channel(image, name):
    """Add chat channel image"""
    CopyImage(image, name, chat_image_dir)


@cli.command()
@click.option("-vc", "--voice-channel", "dir", flag_value=vc_image_dir)
@click.option("-c", "--chat-channel", "dir", flag_value=chat_image_dir)
@click.option("-s", "--server-logo", "dir", flag_value=server_image_dir)
@click.argument('file-index', type=int)
def remove_image(file_index, dir):
    """Remove image"""
    if dir != None:
        image = os.listdir(dir)
        os.remove(f"{dir}\\{image[file_index-1]}")
        click.echo(
            f"image {click.style(image[file_index-1], fg='yellow')} removed")
    else:
        click.secho("Error: Missing one of these options ", fg="red", nl=False)
        click.secho(
            "['-vc' / '--voice-channel', '-c' / '--chat-channel', '-s' / '--server-image'].", fg='yellow', bold=True)


@cli.command()
@click.option("-d", "--discord", type=click.Path(exists=True), help="Register discord path")
@click.option("-p", "--playlist", type=click.Path(exists=True), help="Register songs in textfile")
def register(discord, playlist):
    """Initialize discord path and song_playlist.txt"""
    # File type and input validation
    try:
        if (playlist == None):
            if (discord.endswith(".exe")):
                with open("discord_path.txt", "w") as file:
                    file.write(discord)

        elif (discord == None):
            if (playlist.endswith(".txt")):
                with open("playlist.txt", "a") as file:
                    file.write(playlist + "\n")

        elif (discord.endswith(".exe") and playlist.endswith(".txt")):
            with open("discord_path.txt", "w") as file:
                file.write(discord)
            with open("playlist.txt", "a") as file:
                file.write(playlist + "\n")
        else:
            click.secho("ERROR: Invalid file type", fg="red")
    # If playlist.txt don't exist or deleted(just in case). Create a new one
    except FileNotFoundError:
        with open("playlist.txt", "w") as file:
            file.write(playlist + "\n")


@cli.command()
def view():
    """View list images"""

    # List all the file in the images sub-directory.
    # ==================================================
    # list the file inside voice_channel directory
    click.secho("\nVoice Channel", fg='cyan', bold=True, underline=True)
    if len(os.listdir(vc_image_dir)) != 0:
        for index, file in enumerate(os.listdir(vc_image_dir)):
            filename, file_extension = os.path.splitext(file)
            click.secho(f"  {index+1}. " + filename, fg='bright_green')
    else:
        click.secho("  none", fg='red')

    # list the file inside server_img directory
    click.secho("\nServer", fg='cyan', bold=True, underline=True)
    if len(os.listdir(server_image_dir)) != 0:
        for index, file in enumerate(os.listdir(server_image_dir)):
            filename, file_extension = os.path.splitext(file)
            click.secho(f"  {index+1}. " + filename, fg='bright_green')
    else:
        click.secho("  none", fg='red')

    # list the file inside chat_channel directory
    click.secho("\nChat Channel", fg='cyan', bold=True, underline=True)
    if (len(os.listdir(chat_image_dir)) != 0):
        for index, file in enumerate(os.listdir(chat_image_dir)):
            filename, file_extension = os.path.splitext(file)
            click.secho(f"  {index+1}. " + filename, fg='bright_green')
    else:
        click.secho("  none", fg='red')

    # List the playlist inside playlist.txt
    click.secho("\nPlaylist", fg="cyan", bold=True, underline=True)
    try:
        with open(".\\dmat\\playlist.txt", "r") as file:
            file_content = file.read()
            splitted_content = file_content.split('\n')

            # Check if the file is empty
            if splitted_content != ['']:
                for index, playlist in enumerate(splitted_content):
                    # If the list is not empty
                    if len(playlist) > 1:
                        # Normalize the path from "\\" to "\" and
                        # turn it into a list based on "\"
                        playlist_path = os.path.normpath(playlist).split(os.sep)

                        click.secho(f"  {index+1}. " +
                                    playlist_path[-1][:-4], fg='bright_green')
                    else:
                        continue
                # Add spacing
                else:
                    click.echo("")
            else:
                click.secho("  none\n", fg='red')
    except FileNotFoundError:
        click.secho("  File doesn't exist\n", fg='red')

if __name__ == '__main__':
    cli()
