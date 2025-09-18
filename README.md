<p align="center">
  <a href="https://github.com/pthndv/pyrofast">
    <img src="https://github.com/pthndv/Pyrofast/pyrofast-logo.png" alt="Pyrofast" width="128">

  </a>
  <br>
  <b>Telegram MTProto API Framework for Python</b>
  <br>
  <a href="#">Homepage</a> •
  <a href="#">Documentation</a> •
  <a href="#">Releases</a> •
  <a href="#">News</a>
</p>

# Pyrofast - A fast fork of Pyrogram

Copyright (C) 2025 Ray

This file is part of PyroFast.

Pyrofast is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

---

> [!NOTE]  
> Pyrofast is under active development. Expect rapid changes and improvements.

**Pyrofast** is a modern, elegant, and asynchronous [MTProto API](https://core.telegram.org/mtproto) framework.  
It enables you to interact with the Telegram API using user accounts or bot identities, with **simplicity and speed** in mind.

Pyrofast is a fork of [Pyrogram](https://github.com/pyrogram/pyrogram), built for performance and cleaner syntax.

---

## Example

```python
from pyrofast import Bot

bot = Bot("mi_bot")

@bot.on_message()
async def hello(msg):
    await msg.reply("Hello from Pyrofast!")

bot.run()
