# 🔐 PassForge — Password Generator & Encoder

PassForge is a dual-mode (CLI + GUI) tool to generate secure passwords using common encoding algorithms such as Base64, Hex, Unicode, MD5, SHA1, and SHA256. It supports truncation and appending custom symbols to the outputs.

---

## 🧰 Features

- Encode input using Base64, Unicode, ASCII, MD5, SHA1, SHA256  
- Append custom symbols to encoded outputs  
- Optionally truncate the encoded string length  
- Supports both GUI and Command-line interfaces  
- Clipboard copy support (requires `pyperclip`)

---

## 🚀 Usage

### Run GUI Mode

```bash
python3 pass_forge.py
````

### Run Command-Line Mode

```bash
python3 pass_forge.py -i "Rock411" --symbol "@CNR" --limit 12
```

### Sample Output

```
================= Encoded Results =================
BASE64    : Um9jazQxMQ==@CNR
HEX       : 526f636b343131@CNR
UNICODE   : \u0052\u006f\u0063\u006b\u0034\u0031\u0031@CNR
...
✅ Recommended Password: Um9jazQxMQ==@CNR
```

---

## 📦 Build into Executable (Windows)

Run the following batch script to generate a standalone `.exe`:

```bash
build.bat
```

The resulting executable will be located in the `/dist` directory.

---

## 📥 Dependencies

Install required Python modules with:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Development

* Make sure Python 3.6+ is installed
* For packaging, [PyInstaller](https://www.pyinstaller.org/) is required

---

## 🐞 Issues & Feedback

Please report any issues or feature requests via the [GitHub Issues](https://github.com/Dai411/Toolbox/issues) page.

---

## 📜 License

MIT © 2025 Lining YANG

---


