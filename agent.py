import os
import subprocess
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest

BOT_TOKEN = "8989887535:AAGX4N1U18w1KrbkMX_cOr0Y90otZvD7qsc"
OLLAMA_URL = "http://localhost:11434/api/generate"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text: return
    user_text = update.message.text
    system_prompt = (
        "You are RobLadCrab, a self-sufficient AI Agent running locally on a smartphone via Termux. "
        "You have direct access to the local Linux terminal shell. If the user asks you to execute a task "
        "that requires a bash command, respond exactly with 'CMD: your_command_here'. Otherwise, reply normally."
    )
    payload = {"model": "llama3.2:1b", "prompt": f"{system_prompt}\n\nUser: {user_text}\nAgent:", "stream": False}
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60).json()
        ai_reply = response.get("response", "")
    except Exception:
        await update.message.reply_text("⚠️ Local Brain Error: Ollama timed out.")
        return
    if ai_reply.startswith("CMD:"):
        cmd = ai_reply.replace("CMD:", "").strip()
        await update.message.reply_text(f"🦀 **RobLadCrab tool deployment:** Running `{cmd}`...")
        try:
            result = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT, timeout=15)
            payload["prompt"] += f"\nResult of command: {result}\nAgent final answer:"
            final_response = requests.post(OLLAMA_URL, json=payload, timeout=60).json()
            await update.message.reply_text(final_response.get("response", "Task complete."))
        except Exception as e:
            await update.message.reply_text(f"❌ Shell Execution error: {str(e)}")
    else:
        await update.message.reply_text(ai_reply)

def main():
    tg_request = HTTPXRequest(connect_timeout=15.0, read_timeout=20.0)
    app = Application.builder().token(BOT_TOKEN).request(tg_request).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("⚡ RobLadCrab Autonomous Agent is live and listening on the grid...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
