# ttsrelay

listens for discord messages from beyond 20. 

parses their embeds, then [reposts it to tabletop simulator via the port 39999 external editor integration](https://api.tabletopsimulator.com/externaleditorapi/).

to configure bot, edit `options.py` directly. it's got some documentation.

it needs python 3.8 and a few dependencies. you can make an environment capable of running the code in windows with the `environment.yml` file.

note: it will not work on linux because of [reasons](https://forums.tabletopsimulator.com/showthread.php?5526-Linux-External-Editor-API)

