#!/data/data/com.termux/files/usr/bin/sh
python ~/news_agent/news_agent.py > ~/news_agent/output.txt
termux-notification --id technews --title "Tech News" --content "$(cat ~/news_agent/output.txt)"