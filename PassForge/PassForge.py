import sys
import argparse
import hashlib
import base64
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import colorama
colorama.init()
use_color = True

# Check if pyperclip is available for clipboard operations
# If not, we will skip clipboard functionality
# This is useful for environments where clipboard access is not needed or available.
# If you want to use clipboard, install pyperclip via pip: pip install pyperclip
"""
Password Generator Tool

Author: Lining YANG @ CNR-ISMAR, BOLOGNA, ITALY
Date: 2025-07-28
Last Modified: 2025-07-28
License: MIT License

Description:
    - Generates encoded or hashed versions of an input string (e.g. master password + site)
    - Supports Base64, Hex, Unicode, ASCII decimal, MD5, SHA1, SHA256 outputs
    - Automatically appends user-defined special symbols to all outputs
    - Provides a recommended password (truncated Base64 + symbol)
    - Supports both command-line interface (CLI) and graphical user interface (GUI)
    - CLI options to save output to file and copy recommended password to clipboard (requires pyperclip)
    - GUI includes easy input, output display, and copy button

Usage examples (CLI):
    python3 PassForge.py -i "Rock411Gmail" --limit 12 --symbol "@CNR" --mode all --copy
    python3 PassForge.py -i "Rock411Gmail" --mode md5

Run without arguments to open the GUI window.

Requires Python 3.x.
"""

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

def add_symbol_to_value(value, symbol):
    """Append special symbol to the encoding/hash value if symbol is provided."""
    return value + (symbol if symbol else "")

def encode_all_modes(input_str, symbol=None):
    """
    Encode input string into multiple modes.
    All outputs will append the special symbol if provided.
    """
    results = {
        "base64": base64.b64encode(input_str.encode()).decode(),
        "hex": input_str.encode().hex(),
        "unicode": ''.join(['\\u{:04x}'.format(ord(c)) for c in input_str]),
        "ascii": ' '.join([str(ord(c)) for c in input_str]),
        "md5": hashlib.md5(input_str.encode()).hexdigest(),
        "sha1": hashlib.sha1(input_str.encode()).hexdigest(),
        "sha256": hashlib.sha256(input_str.encode()).hexdigest()
    }
    if symbol:
        for key in results:
            results[key] = add_symbol_to_value(results[key], symbol)
    return results

def generate_recommendation(base64_encoded, limit, symbol):
    """
    Generate recommended password by truncating Base64 output,
    and appending the special symbol if provided.
    """
    base64_part = base64_encoded[:limit] if limit else base64_encoded
    return base64_part + (symbol if symbol else "")

def format_output(results, recommend, symbol=None, use_color=True):
    """
    Format the output with colored and aligned text,
    includes dividing lines and highlights recommended password.
    """
    RESET = "\033[0m" if use_color else ""
    BOLD = "\033[1m" if use_color else ""
    CYAN = "\033[36m" if use_color else ""
    GREEN = "\033[32m" if use_color else ""
    YELLOW = "\033[33m" if use_color else ""
    LINE = CYAN + ("-" * 50) + RESET

    lines = [LINE]
    lines.append(f"{BOLD}{'Encoding Type':<12} | Result{RESET}")
    lines.append(LINE)

    for k, v in results.items():
        if symbol and v.endswith(symbol):
            core = v[:-len(symbol)]
            suffix = symbol
            if use_color:
                line = f"{k.upper():<12} | {core}{YELLOW}{suffix}{RESET}"
            else:
                line = f"{k.upper():<12} | {core}{suffix}"
        else:
            line = f"{k.upper():<12} | {v}"
        lines.append(line)

    lines.append(LINE)
    lines.append(f"{GREEN}✅ Recommended Password:{RESET} {BOLD}{recommend}{RESET}")
    lines.append(LINE)
    return "\n".join(lines)

def run_cli():
    """
    Command-line interface handler.
    Usage example:
      python3 script.py -i "master+site" --limit 12 --symbol "@!" --mode all --copy
    """
    parser = argparse.ArgumentParser(description="Generate encoded passwords based on input string")
    parser.add_argument('-i', '--input', required=True, help='Input string (e.g. master password + site name)')
    parser.add_argument('--limit', type=int, help='Number of Base64 characters to keep in recommended password')
    parser.add_argument('--symbol', type=str, help='Additional special symbol(s) to append')
    parser.add_argument('--mode', type=str, choices=['base64', 'hex', 'unicode', 'ascii', 'md5', 'sha1', 'sha256', 'recommend', 'all'], default='all', help='Output encoding mode')
    parser.add_argument('--output', type=str, help='Write output to file')
    parser.add_argument('--copy', action='store_true', help='Copy recommended password to clipboard (requires pyperclip)')

    args = parser.parse_args()
    input_str = args.input
    all_results = encode_all_modes(input_str, args.symbol)
    recommend = generate_recommendation(all_results['base64'], args.limit or 12, args.symbol)

    if args.mode == 'all':
        output_text = format_output(all_results, recommend, args.symbol, use_color=True)
    elif args.mode == 'recommend':
        output_text = f"✅ Recommended Password: {recommend}"
    else:
        output_text = f"{args.mode.upper()} : {all_results[args.mode]}"

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"\n📁 Output saved to file: {args.output}")
    else:
        print(output_text)

    if args.copy:
        if CLIPBOARD_AVAILABLE:
            pyperclip.copy(recommend)
            print("📋 Recommended password copied to clipboard")
        else:
            print("⚠️ Please install pyperclip module: pip install pyperclip")

def run_gui():
    """
    Graphical User Interface for password generator.
    Run without command-line arguments to launch the window.
    """
    def on_generate():
        input_str = entry_input.get().strip()
        if not input_str:
            messagebox.showwarning("Warning", "Please enter the input string!")
            return
        limit = None
        if entry_limit.get():
            try:
                limit = int(entry_limit.get())
            except ValueError:
                messagebox.showwarning("Warning", "Limit must be an integer!")
                return
        symbol = entry_symbol.get()
        mode = combo_mode.get()

        all_results = encode_all_modes(input_str, symbol)
        recommend = generate_recommendation(all_results['base64'], limit or 12, symbol)

        if mode == 'all':
            output_text = format_output(all_results, recommend, symbol, use_color=False)
        elif mode == 'recommend':
            output_text = f"✅ Recommended Password: {recommend}"
        else:
            output_text = f"{mode.upper()} : {all_results[mode]}"

        text_result.config(state='normal')
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, output_text)
        text_result.config(state='disabled')

    def on_copy():
        text = text_result.get(1.0, tk.END).strip()
        if not text:
            messagebox.showinfo("Info", "No content to copy!")
            return
        if CLIPBOARD_AVAILABLE:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Content copied to clipboard")
        else:
            messagebox.showwarning("Warning", "Please install pyperclip module to enable copy functionality")

    root = tk.Tk()
    root.title("Password Generator")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    # Assign grid layout to the frame
    frame.grid_rowconfigure(5, weight=1)  # ScrolledText stretchable
    frame.grid_columnconfigure(1, weight=1)  # Firstt column stretchable

    # Input grid
    ttk.Label(frame, text="Input string (master password + site):").grid(row=0, column=0, sticky=tk.W)
    entry_input = ttk.Entry(frame, width=40)
    entry_input.grid(row=0, column=1, sticky=tk.EW)  # Horizontal stretch
    entry_input.insert(0, "Penrhyn@Slate")

    ttk.Label(frame, text="Base64 truncate length:").grid(row=1, column=0, sticky=tk.W)
    entry_limit = ttk.Entry(frame, width=10)
    entry_limit.grid(row=1, column=1, sticky=tk.W)
    entry_limit.insert(0, "12")

    ttk.Label(frame, text="Additional special symbol(s):").grid(row=2, column=0, sticky=tk.W)
    entry_symbol = ttk.Entry(frame, width=10)
    entry_symbol.grid(row=2, column=1, sticky=tk.W)
    entry_symbol.insert(0, "@!")

    ttk.Label(frame, text="Output mode:").grid(row=3, column=0, sticky=tk.W)
    combo_mode = ttk.Combobox(frame, values=['all', 'base64', 'hex', 'unicode', 'ascii', 'md5', 'sha1', 'sha256', 'recommend'], state='readonly')
    combo_mode.grid(row=3, column=1, sticky=tk.W)
    combo_mode.current(0)

    btn_generate = ttk.Button(frame, text="Generate Password", command=on_generate)
    btn_generate.grid(row=4, column=0, columnspan=2, pady=5)

    text_result = scrolledtext.ScrolledText(frame, width=60, height=15, state='disabled')
    text_result.grid(row=5, column=0, columnspan=2, pady=5, sticky=tk.NSEW)  # Modified to use ScrolledText

    btn_copy = ttk.Button(frame, text="Copy Result", command=on_copy)
    btn_copy.grid(row=6, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    # If command line args exist, run CLI, else launch GUI window
    if len(sys.argv) > 1:
        run_cli()
    else:
        run_gui()
