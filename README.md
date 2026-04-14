# AI-Agent_PersonalNews
AI agent per il recupero di notizie personalizzate

Scaricare Termix, Termux:Widget e Tasker
in termux:
pkg update
pkg install git cmake build-essential
pkg install python
-- Scarichiamo llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make

-- scaricarlo da HuggingFace (gratuito)
mkdir ~/models
cd ~/models
wget https://huggingface.co/Qwen/Qwen2.5-1.5B-GGUF/resolve/main/qwen2.5-1.5b-q4_k_m.gguf
-- Installa il binding Python:
pip install llama-cpp-python
