import docker, json
from colorama import Fore
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

rd = Fore.RED
bl = Fore.BLACK
w = Fore.WHITE
def load_conf(filepath="config.json"):
    with open(filepath, "r") as f:
        return json.load(f)

def get_docker_logic():
    try:
        client = docker.from_env()
        containers = client.containers.list(all=True)
        report = "*Current status of containers:*\n"
        for c in containers:
            status_moji = "🟢" if c.status == "running" else "🔴"
            report += f"{status_moji} *{c.name}*\n      Status: `{c.status}`\n"
        return report
    except Exception as e:
        return f"{bl}[{w}!{bl}] {rd}{e}"

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config = load_conf()
    if str(update.effective_chat.id) != str(config.get("chatid")):
        await update.message.reply_text("Unknown Chat")
        return

    report = get_docker_logic()
    await update.message.reply_text(report, parse_mode="Markdown")

def main():
    config = load_conf()
    token = config.get("token")
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("status", status_command))
    application.run_polling()

if __name__ == "__main__":
    main()