# 💖 Overwatch !rank command for Streamer.bot 

This is a little setup I made for myself that lets people type `!rank` in Twitch chat and see the streamer's current **Overwatch 2 competitive ranks and winrate**.
It works with [Streamer.bot](https://streamer.bot/) and uses [timomak's Overwatch API](https://github.com/timomak/Overwatch-API) to grab the data.

The information gets saved to a `.txt` file that is then displayed with Streamer.bot.

---

## What This Includes

- A Python script that pulls OW2 data from the API
- A text file with the import code for Streamer.bot

---

## How to Use It

### 1. Download the Files

You can clone this repo or just grab the files manually:
- `overwatch_rank_fetcher.py`
- `streamerbot_action.txt` (the Streamer.bot action)
Just put it in a folder and you're good.

---

### 2. Install Python and Requests

#### Check if Python is installed:

- Open **Command Prompt** (on Windows) or **Terminal** (on Mac)
- Type:
```bash
python --version
```

If it says something like `'python' is not recognized as an internal or external command`
then you’ll need to install Python from here: https://www.python.org/downloads/


Once its installed, in the same Command Prompt/Terminal window:
```bash
pip install requests
```

---

### 3. Edit the .py File With Your Player Info

- Open the `.py` file with Notepad
- Replace `username-12345` with your battletag (use `-` instead of the `#`)


---

### 4. Import the Streamer.bot Action

1. Open Streamer.bot
2. Click **Import**
3. Copy the string in `streamerbot_action.txt`

After importing, in the Commands tab, make sure the `get OW rank` command is enabled (right-click on it and make sure enabled is checked).

After typing !rank in chat, it should resemble something like this:
♡⸜(˶˃ ᵕ ˂˶)⸝♡ player’s current Overwatch ranks are:
Tank: Gold 1 | Damage: Platinum 4 | Support: Diamond 2
🎯 Competitive winrate: 51.6%

## ❗ Important Notes

- 📍 **Only works for US region** by default  
  If you want a different region, just change the `us` part of the API URL to `eu` etc. in the .py script.
- ⚙️ This was made to run locally on your PC with Streamer.bot.
