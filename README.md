# py-nano-id

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-nano-id/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency, cryptographically secure, URL-friendly compact unique string ID generator in pure Python.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python standard library (`secrets`).
- 🔐 **Cryptographically Secure**: Hardware entropy via `secrets.choice`.
- 📏 **Compact & URL-Friendly**: 21-character alphabet (`A-Za-z0-9_-`).

---

## 📦 Installation

```bash
pip install py-nano-id
```

---

## 🛠️ Quickstart

```python
from py_nano_id import generate_id

id1 = generate_id()
print(id1)  # V1StGXR8_Z5jdHi6B-myT

id_short = generate_id(size=10)
print(id_short)  # 10 characters
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this nano ID generator simplified your primary keys, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
