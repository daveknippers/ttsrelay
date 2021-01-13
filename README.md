# ttsrelay

listens for discord messages from beyond 20. 

parses their embeds, then [reposts it to tabletop simulator via the port 39999 external editor integration](https://api.tabletopsimulator.com/externaleditorapi/).

to configure bot, edit `options.py` directly. it's got some documentation.

add your discord bot's connection token in the `tokens.py` file.

it needs python 3.8. you'll need the `discord.py` module, available from pip [here](https://pypi.org/project/discord.py/). alternatively you can make a conda environment capable of running the code in windows with the `environment.yml` file. 

note: it will not work on linux because of [reasons](https://forums.tabletopsimulator.com/showthread.php?4556-External-Integration-Bug-Linux)

