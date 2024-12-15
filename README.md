# Text Formatter Bot

A Telegram bot for converting user-input text into beautifully formatted Markdown or HTML. This bot is designed to be simple, efficient, and highly functional for anyone who wants to experiment with text formatting styles in real time.

---

## Features

1. **Markdown and HTML Formatting**:
   - Supports common Markdown styles like bold (`**bold**`), italic (`*italic*`), strikethrough (`~~text~~`), links (`[text](url)`), and inline code (`\`code\``).
   - Converts the input into either Markdown or HTML based on user preference.

2. **Interactive Commands**:
   - `/start` or `/help`: Displays instructions on how to use the bot.
   - `/set_html`: Switches the output format to HTML.
   - `/set_markdown`: Switches the output format back to Markdown.

3. **Error Handling**:
   - Safely handles unexpected inputs or formatting errors.

4. **Customizable Code**:
   - Easily extend the bot to include more formatting features such as headers or blockquotes.

---

## Installation

Follow these steps to install and set up the bot:

### Prerequisites
- Python 3.7+
- A Telegram bot token from the [BotFather](https://core.telegram.org/bots#botfather).

### Clone the Repository
```bash
# Clone this repository
git clone https://github.com/your-username/telegram-text-formatter-bot.git
cd telegram-text-formatter-bot
```

### Set Up a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Linux/MacOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Your Bot Token
1. Open the `bot.py` file.
2. Replace `YOUR_BOT_TOKEN` with the token you received from the BotFather.

### Run the Bot
```bash
python bot.py
```
The bot will start and display `Bot is running...` in the terminal.

---

## Usage

### Start the Bot
Once the bot is running, open Telegram and start a chat with your bot. Use the following commands:

- `/start` or `/help`: Learn how to use the bot.
- `/set_html`: Switch the output format to HTML.
- `/set_markdown`: Switch back to Markdown.

### Send Text to Format
Send a message using Markdown-style formatting, such as:
```plaintext
This is **bold**, *italic*, ~~strikethrough~~.
Visit [Google](https://google.com).
Inline code: `print("Hello World")`
```

### Output Examples
#### Markdown Output:
```plaintext
This is **bold**, *italic*, ~~strikethrough~~.
Visit [Google](https://google.com).
Inline code: `print("Hello World")`
```

#### HTML Output:
```html
This is <b>bold</b>, <i>italic</i>, <s>strikethrough</s>.
Visit <a href="https://google.com">Google</a>.
Inline code: <code>print("Hello World")</code>
```

---

## File Structure
```plaintext
.
├── bot.py             # Main bot script
├── README.md          # Project documentation
├── requirements.txt   # Dependencies list
```

---

## Extending the Bot
This bot is modular and easy to extend. You can:
- Add support for headers (`# Header`), blockquotes (`> Quote`), or lists.
- Integrate database support to remember user preferences across sessions.
- Add more error-handling capabilities.

---

## Dependencies
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [re (Regular Expressions)](https://docs.python.org/3/library/re.html)

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## License
This project is licensed under the MIT License.

---

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to improve this bot.

