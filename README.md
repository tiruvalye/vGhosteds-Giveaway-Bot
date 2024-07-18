# vGhosted's Giveaway Bot

Welcome to vGhosted's Giveaway Bot, designed to facilitate giveaways on the Discord server for viewers of vGhosted's streams on Twitch and Kick. This project is led by **Petalprism** with **CptSmirk** as the co-lead.

## Overview

vGhosted's Giveaway Bot is a Discord bot created to manage and run giveaways, enhancing the interaction during vGhosted's streams. This bot is currently under active development.

## Key Features

- **Automated Giveaways**: Easily set up and manage giveaways with commands.
- **Role-Based Access**: Only authorized users can start and manage giveaways.
- **Logging**: Command usage and errors are logged for transparency and debugging.
- **Slash Commands**: Utilize Discord's slash command interface for ease of use.
- **Flexible Configuration**: Configure various settings through a configuration file.

## Installation

### Prerequisites

- Python 3.8+
- Git
- Virtual Environment (venv)

### Steps

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/tiruvalye/vghosteds-giveaway-bot.git
   cd vghosteds-giveaway-bot
   ```

2. **Create a Virtual Environment:**
   ```sh
   python3 -m venv vggiveaway_venv
   source vggiveaway_venv/bin/activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

Create a `config.py` file in the project directory and add your configuration details:

```python
BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Discord Role IDs
giftmod_role_id = 1215916915055136798

# Discord Channel IDs
giveaways_channel_id = 1263359243839340576
giftlogs_channel_id = 1263359265926680607
```

## Usage

### Running the Bot

Activate the virtual environment and run the bot:

```sh
source vggiveaway_venv/bin/activate
python3 bot.py
```

### Commands

#### !hello
- **Description:** Greets the user.
- **Usage:** `!hello`

#### /hello
- **Description:** Greets the user with a slash command.
- **Usage:** `/hello`

### Permissions

Only users with the `giftmod_role_id` can use the bot commands.

## Contributing

We welcome contributions to vGhosted's Giveaway Bot! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact the project lead, Petalprism, or the co-lead, CptSmirk.