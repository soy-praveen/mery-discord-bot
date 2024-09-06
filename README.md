# Mery Price Discord Bot

This Discord bot fetches the real-time price of the cryptocurrency "Mery" from the Cronos chain using the DexScreener API. It also updates the bot's nickname with the current price and responds to specific messages in the server.

## Features

- Responds to user messages containing the keywords "mery price" or "mistery price."
- Fetches the current price of Mery using the DexScreener API.
- Displays the 1-hour, 6-hour, and 24-hour percentage price changes.
- Updates the bot's nickname to the current price of Mery.
- Deletes the error message after 120 seconds if the price cannot be fetched.

## Prerequisites

Make sure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/)
- [Discord.py](https://discordpy.readthedocs.io/en/stable/)
- A valid bot token from Discord
- Access to the [DexScreener API](https://docs.dexscreener.com/)

## Installation

1. Clone this repository or download the source files.

    ```bash
    git clone https://github.com/your-username/mery-price-discord-bot.git
    cd mery-price-discord-bot
    ```

2. Install the required Python packages using `pip`:

    ```bash
    pip install discord.py requests aiohttp
    ```

3. Set up your environment:

    - Replace `'MERY_BOT_TOKEN'` in the code with your actual Discord bot token.

4. (Optional) If you want to change the cryptocurrency or API endpoint, update the `url` in the bot code with the appropriate API URL.

## Usage

1. Run the bot by executing the following command in your terminal:

    ```bash
    python bot.py
    ```

2. Invite the bot to your server using the OAuth2 URL from Discord Developer Portal with the proper permissions.

3. Once the bot is added, it will listen to messages in the server. If anyone sends a message that includes the keywords `mery price` or `mistery price`, the bot will respond with the current price and recent percentage changes.

4. The bot will automatically update its nickname to reflect the latest price of Mery on the server.

## Bot Permissions

Ensure your bot has the following permissions enabled in your Discord server:

- `Change Nickname`
- `Send Messages`
- `Embed Links`

## Example

![Screenshot-1](https://github.com/soy-praveen/mery-discord-bot/blob/main/Screenshot%202024-06-17%20234150.png)
