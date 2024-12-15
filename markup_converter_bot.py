import re
import telebot

# Initialize the bot with your token
TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot("7897904789:AAGdI3uhkuKqZsVHylphtKG64mtJJw3MrxA")

# User preferences for output format (Markdown or HTML)
user_preferences = {}

# Function to handle formatting
def format_text(user_input, output_format="markdown"):
    if output_format == "markdown":
        # Markdown formatting
        formatted_text = user_input
        formatted_text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', formatted_text)  # Bold
        formatted_text = re.sub(r'\*(.*?)\*', r'*\1*', formatted_text)        # Italic
        formatted_text = re.sub(r'~~(.*?)~~', r'~~\1~~', formatted_text)      # Strikethrough
        formatted_text = re.sub(r'`(.*?)`', r'`\1`', formatted_text)          # Inline code
        formatted_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'[\1](\2)', formatted_text)  # Links
        return formatted_text

    elif output_format == "html":
        # HTML formatting
        formatted_text = user_input
        formatted_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', formatted_text)  # Bold
        formatted_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', formatted_text)      # Italic
        formatted_text = re.sub(r'~~(.*?)~~', r'<s>\1</s>', formatted_text)      # Strikethrough
        formatted_text = re.sub(r'`(.*?)`', r'<code>\1</code>', formatted_text)  # Inline code
        formatted_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', formatted_text)  # Links
        return formatted_text

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Welcome to the Text Formatter Bot! 🎉\n"
        "You can send me text with Markdown formatting like:\n"
        "- **Bold** (e.g., `**bold**`)\n"
        "- *Italic* (e.g., `*italic*`)\n"
        "- ~~Strikethrough~~ (e.g., `~~strikethrough~~`)\n"
        "- [Links](https://example.com) (e.g., `[text](url)`)\n"
        "- `Inline Code`\n\n"
        "By default, I reply in Markdown. You can switch to HTML by sending `/set_html`.\n"
        "Switch back to Markdown with `/set_markdown`."
    )

@bot.message_handler(commands=['set_html'])
def set_html(message):
    user_preferences[message.chat.id] = "html"
    bot.reply_to(message, "Output format set to HTML. ✅")

@bot.message_handler(commands=['set_markdown'])
def set_markdown(message):
    user_preferences[message.chat.id] = "markdown"
    bot.reply_to(message, "Output format set to Markdown. ✅")

@bot.message_handler(func=lambda message: True)
def process_message(message):
    user_id = message.chat.id
    user_input = message.text

    # Get user preference (default: Markdown)
    output_format = user_preferences.get(user_id, "markdown")

    # Format the text
    try:
        formatted_text = format_text(user_input, output_format)
        if output_format == "markdown":
            bot.reply_to(message, formatted_text, parse_mode="Markdown")
        elif output_format == "html":
            bot.reply_to(message, formatted_text, parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Start polling
print("Bot is running...")
bot.infinity_polling()
