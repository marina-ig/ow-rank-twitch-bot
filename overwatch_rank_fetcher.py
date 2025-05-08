import requests
import random
import sys
import os

# 🛠 SET YOUR BATTLETAG HERE
battletag = "username-12345"  # Replace with your battletag

# 📛 This will be used in messages
display_name = battletag.split("-")[0]  

# 🌍 API endpoint from https://github.com/timomak/Overwatch-API
url = f"https://ow-api.com/v1/stats/pc/us/{battletag}/profile"

# (´｡• ᵕ •｡`)♡ Cute kaomojis
happy_kaomojis = [
    "(๑>◡<๑)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(｡•̀ᴗ-)✧", "( ˶ˆᗜˆ˶ )", "♡⸜(˶˃ ᵕ ˂˶)⸝♡", "⋆˚✿˖°",
    "٩(｡•́‿•̀｡)۶", "ദ്ദി(｡•̀ ,<)~✩‧₊", "♡(੭´͈ ᐜ `͈)੭", "ฅ^>⩊<^ ฅ"
]

sad_kaomojis = [
    "(´；д；`)", "(◞‸◟；)", "(｡•́︿•̀｡)", "(╯︵╰,)", "( • ᴖ • ｡)", "(￣ヘ￣;)",
    ".·°՞(っ-ᯅ-ς)՞°·.", "｡°(°.◜ᯅ◝°)°｡"
]

try:
    res = requests.get(url, timeout=5)
    data = res.json()

    if data.get("private") or "ratings" not in data or not data["ratings"]:
        output = f"{random.choice(sad_kaomojis)} Sorry! {display_name}’s Overwatch profile is private or unranked~"
    else:
        # Prepare rank info
        rank_lines = []
        for role in data["ratings"]:
            role_name = role["role"].capitalize()
            rank_group = role["group"]
            tier = role["tier"]
            rank_lines.append(f"{role_name}: {rank_group} {tier}")

        # Calculate winrate
        games_played = data.get("competitiveStats", {}).get("games", {}).get("played", 0)
        games_won = data.get("competitiveStats", {}).get("games", {}).get("won", 0)
        winrate = (games_won / games_played) * 100 if games_played > 0 else 0

        # Output message
        face = random.choice(happy_kaomojis)
        output = f"{face} {display_name}'s current Overwatch ranks are:\n" + \
                 " | ".join(rank_lines) + \
                 f"\n🎯 Competitive winrate: {winrate:.1f}%"

    # 📝 Save to file next to script
    with open(os.path.join(os.path.dirname(__file__), "ow_rank_output.txt"), "w", encoding="utf-8") as f:
        f.write(output)

except Exception as e:
    output = f"{random.choice(sad_kaomojis)} Failed to fetch Overwatch rank.\nError: {e}"
    with open(os.path.join(os.path.dirname(__file__), "ow_rank_output.txt"), "w", encoding="utf-8") as f:
        f.write(output)
