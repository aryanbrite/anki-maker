<p align="center">
  <img src="https://cdn.hackclub.com/019e7958-7190-7083-84ae-d86b4bff3f24/pngwing.com.png" width="128" height="128" alt="Anki AI">
</p>

<h1 align="center">Anki AI</h1>

<p align="center">
  Turn Medical Notes into Anki Cards in Seconds for Free :)
</p>
<p align="center">

  <img alt="Python" src="https://img.shields.io/badge/Python-3-blue?logo=python" />
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-635bff?logo=streamlit&logoColor=white" />
  <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" />
  <a href="https://summer.hackclub.com/projects/10572">
    <img alt="Hack Club Batch" src="https://img.shields.io/badge/Hack%20Club-Project-red?style=flat&logo=hackclub&logoColor=white" />
  </a>
</p>

---


<p align="center">
  <i>This is a Python based Anki Cards generator which generates cards using any PDF. An average Medical Student/Doctor/Surgeon spends over 4 hours making and revising Anki Cards. Anki AI makes it easier. You can just upload your pdf and get a well converted Anki Card. </i>
</p>

---

## Quick Start
```bash
git clone https://github.com/aryanbrite/anki-maker
cd anki-maker
pip install uv
uv sync
uv pip install -r requirements.txt
```

Add secrets (IMPORTANT)

Create a file:

```
.streamlit/secrets.toml
```

Example:

```toml
gemini_api = "your_api_key_here"
```
## Run App
```
uvx streamlit run main.py
```

## Tech Stack
- Python
- Streamlit
- PDFPluber
- Pandas

## License
This project is licensed under the MIT License.
© Aryanbrite — aryanbrite@gmail.com