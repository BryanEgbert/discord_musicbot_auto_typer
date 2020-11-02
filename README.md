# discord_musicbot_auto_typer
This is a personal project that automatically write play[url] command for Groovy music bot in discord server.

## Commands
- `main`\
This is the main function that click the server logo, voice channel, chat channel and type the songs for you.
  - `-pre/--prefix` STRING | **Required**\
  A command where you put your server's music bot.
  - `-vc` INTEGER | **Default: 1**\
  A command where you choose which voice channel you want to connect.
  - `-c/--chat` INTEGER | **Default: 1**\
  A command where you choose which chat-channel you want to type the songs in.
  - `-s/--server` INTEGER | **Default: 1**\
  A command where you choose which server to begin the execution.
  - `-play/--playlist` INTEGER | **Required**\
  A command where you choose which playlist to type.

- `add-vc` **PATH**\
A command where you add image of your server's voice channel.
  - `-n/--name` **STRING**\
  A command where you rename the copied image file.

- `add-logo` **PATH**\
A command where you add your server's logo.
  - `-n/--name` STRING\
  A command where you rename the copied image file.

- `add-channel` **PATH**\
A command where you add your server's chat channel.
  - `-n/--name` STRING\
  A command where you rename the copied image file.

- `remove-image` **INTEGER**\
A command where you remove a specific image file
  - `-vc/--voice-channel`\
  Use this command if you want to remove image in voice channel list.
  - `-c/--chat-Channel`\
  Use this command if you want to remmove image in chat channel list.
  - `-s/--server-logo`\
  Use this command if you want to remove image in server logo list.

- `register`\
An important command where you declare your discord path and playlist.
  - `-d/--discord` **PATH**\
  A command to declare your discord path.
  - `-p/--playlist` **PATH** | **Required**\
  A command to declare your playlist textfile path.

- `view`\
A command to view list of voice channel, chat channel, and logo. 
