# 🔐 PassForge — Password Generator & Encoder

A dual-mode (CLI + GUI) tool to generate secure passwords using common encoding algorithms such as Base64, Hex, Unicode, MD5, and SHA. Supports truncation and symbol appending.

---

## 🧰 Features

- Encode input using Base64, Unicode, ASCII, MD5, SHA1, SHA256
- Append custom symbols to outputs
- Optionally truncate encoded string
- GUI and Command-line support
- Clipboard copy (requires `pyperclip`)

---

## 🚀 Usage

### Run (GUI)
```bash
python3 PassForge.py
```

### Run (CLI)  
```bash
python3 pass_forge.py -i "Rock411" --symbol "@CNR" --limit 12
```

### Sample Output
```graphql
================= Encoded Results =================
BASE64    : Um9jazQxMQ==@CNR
HEX       : 526f636b343131@CNR
UNICODE   : \u0052\u006f\u0063\u006b\u0034\u0031\u0031@CNR
...
✅ Recommended Password: Um9jazQxMQ==@CNR
```

### 📦 Build into EXE (Windows)
```bash
build.bat
```
Output `.exe` file will be in `/dist`.

### 📥 Dependencies
Install required modeles:
```bash
pip install -r requirements.txt
```

### 📜 License  
MIT © 2025 Lining YANG




