# Agent AI：從李飛飛80頁綜述到2026實戰指南
## 基於 arXiv:2401.03568 + Web-MCP 整合版

[![Paper](https://img.shields.io/badge/Paper-arXiv:2401.03568-b31b1b.svg)](https://arxiv.org/abs/2401.03568)
[![MCP](https://img.shields.io/badge/Protocol-MCP-blue)](https://modelcontextprotocol.io)
[![A2A](https://img.shields.io/badge/Protocol-A2A-green)](https://a2a-protocol.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 一個可直接發佈到 GitHub 的開源課件項目，包含 PPT、逐字稿、語音解讀稿、Web-MCP Demo、講座視頻腳本

### 📦 目錄結構
```
/agent-ai-guide/
├── README.md
├── docs/01-論文精讀-整體論與五模組.md
├── docs/02-挑戰與幻覺治理.md
├── docs/03-2026-Stack-MCP-A2A.md
├── docs/04-記憶層-RAG不等於Memory.md
├── docs/05-應用場景-遊戲機器人醫療企業.md
├── slides/ (13頁PPT HTML版)
├── scripts/逐字稿-繁體.md
├── scripts/語音解讀稿-SSML.md
├── scripts/講座視頻分鏡腳本.md
└── web-mcp-demo/
```

### 🚀 Web-MCP 設置指南 (2026版)
**核心：MCP = USB-C接口，連接能力；A2A = 網線，連接智能體**

三階段：RAG第一，MCP第二，A2A第三

1. 安裝: `npm install @modelcontextprotocol/sdk`
2. 啟動 MCP Server: `python web-mcp-demo/server.py`
3. 註冊 Agent Card: `/.well-known/agent-card.json`
4. 前端: 用 client.html 透過 WebSocket 連接 MCP

### 🎤 如何演講
- PPT已內建逐字稿
- 語音稿SSML可直接餵TTS
- 視頻腳本含分鏡、字幕、代碼演示時間點

### 📄 授權
MIT
