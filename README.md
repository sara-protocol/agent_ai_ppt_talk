# Agent AI: From Fei-Fei Li's 80-Page Survey to 2026 Stack

> 一個可直接授課、開源可復現的 Agent AI 課件項目

[![Paper](https://img.shields.io/badge/Paper-arXiv%3A2401.03568-b31b1b.svg)](https://arxiv.org/abs/2401.03568)
[![MCP](https://img.shields.io/badge/Protocol-MCP%20USB--C%20for%20LLM-blue)](https://modelcontextprotocol.io)
[![A2A](https://img.shields.io/badge/Protocol-A2A%20Linux%20Foundation-green)](https://a2a-protocol.org)
[![Slides](https://img.shields.io/badge/Slides-GitHub%20Pages-orange)](https://sara-protocol.github.io/agent_ai_ppt_talk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

**基於 Stanford HAI 李飛飛團隊 80頁綜述 `arXiv:2401.03568` + 2026 年 MCP / A2A 協議實戰整合版**

包含：13頁可交互HTML幻燈片、5篇論文精讀、完整逐字稿、SSML語音稿、講座視頻分鏡腳本、Web-MCP可運行Demo。

### 🎯 在線閱讀

- **👉 在線看課件（GitHub Pages）：https://sara-protocol.github.io/agent_ai_ppt_talk/**
- **📄 論文原文：https://arxiv.org/abs/2401.03568**
- **💻 Demo：`web-mcp-demo/` 一鍵啟動**

---

## 📦 目錄結構

```
/agent_ai_ppt_talk/
├── README.md                          # 本文件
├── LICENSE                            # MIT 授權
├── .gitignore                         # Git 忽略規則
├── index.html                         # GitHub Pages 首頁（跳轉入口）
│
├── docs/                              # 5篇精讀文檔
│   ├── 01-論文精讀-整體論與五模組.md   # 整體論與五模組：感知/推理/記憶/工具/行動
│   ├── 02-挑戰與幻覺治理.md            # 挑戰、幻覺、評估
│   ├── 03-2026-Stack-MCP-A2A.md       # 2026技術棧：MCP=USB-C, A2A=網線
│   ├── 04-記憶層-RAG不等於Memory.md    # 記憶層深度解析
│   └── 05-應用場景-遊戲機器人醫療企業.md # 應用場景
│
├── slides/                            # 13頁 HTML 幻燈片
│   ├── cover.html                     # 封面
│   ├── agenda.html                    # 大綱
│   ├── definition.html                # 定義
│   ├── modules.html                   # 五模組
│   ├── perception_reasoning.html
│   ├── memory.html
│   ├── mcp_intro.html                 # MCP 介紹
│   ├── mcp_demo.html
│   ├── mcp_vs_a2a.html                # MCP vs A2A
│   ├── a2a_intro.html
│   ├── eval.html
│   ├── production.html
│   └── action_plan.html
│
├── scripts/                           # 演講輔助
│   ├── 逐字稿-繁體.md
│   ├── 語音解讀稿-SSML.md             # 可直接餵 TTS
│   └── 講座視頻分鏡腳本.md
│
└── web-mcp-demo/                      # 可運行 Demo
    ├── server.py                      # MCP Server
    ├── client.html                    # WebSocket 前端
    └── agent-card.json                # A2A Agent Card
```

---

## 🚀 快速開始

### 1. 在線看課件
直接打開：**https://sara-protocol.github.io/agent_ai_ppt_talk/**

本地預覽：
```bash
git clone https://github.com/sara-protocol/agent_ai_ppt_talk.git
cd agent_ai_ppt_talk
python -m http.server 8000
# 瀏覽器打開 http://localhost:8000/slides/cover.html
```

### 2. Web-MCP Demo (2026版)

> 核心隱喻：**MCP = USB-C接口（連接能力），A2A = 網線（連接智能體）**
> 演進路徑：RAG 第一，MCP 第二，A2A 第三

```bash
cd web-mcp-demo

# 安裝依賴
pip install -r requirements.txt
npm install @modelcontextprotocol/sdk

# 啟動 MCP Server
python server.py
# 另一個終端啟動前端
python -m http.server 8000 --directory .
# 打開 http://localhost:8000/client.html
```

- MCP Server 暴露工具：透過 WebSocket 連接 LLM
- Agent Card 註冊：`/.well-known/agent-card.json` 符合 A2A 協議
- 前端：`client.html` 可視化調用鏈

---

## 🎤 如何演講

| 場景 | 用什麼 |
| :--- | :--- |
| **課堂/分享會** | `slides/` 13頁 HTML，直接用瀏覽器全屏演講，內建逐字稿 |
| **錄製視頻** | `scripts/講座視頻分鏡腳本.md` + `scripts/語音解讀稿-SSML.md` 餵 Azure TTS / ElevenLabs |
| **技術培訓** | `docs/03-2026-Stack-MCP-A2A.md` + `web-mcp-demo/` 現場 Live Coding |
| **論文研讀** | `docs/01-論文精讀-整體論與五模組.md` + 原文 `arXiv:2401.03568` |

---

## 📚 理論基礎

本課件基於：

**Fei-Fei Li et al., "Agent AI: Surveying the Horizons of Multimodal Interaction", arXiv:2401.03568 (2024)**

```bibtex
@article{during2024agentai,
  title={Agent AI: Surveying the Horizons of Multimodal Interaction},
  author={During, Zane and others},
  journal={arXiv preprint arXiv:2401.03568},
  year={2024}
}
```

擴展至 2026 實戰：

- **MCP (Model Context Protocol)** - Anthropic 發起，2024-11發佈，已成 LLM 工具標準 [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **A2A (Agent-to-Agent)** - Google 發起，捐贈給 Linux Foundation [a2a-protocol.org](https://a2a-protocol.org)

---

## 🛠️ 技術棧

- **幻燈片**：原生 HTML + Tailwind CSS + 響應式設計
- **Demo**：Python MCP SDK + WebSocket + A2A Agent Card
- **語音**：SSML 標準，兼容 Azure / AWS Polly / ElevenLabs
- **部署**：GitHub Pages 零配置

---

## 🤝 貢獻

PRs Welcome！

1. Fork 本倉庫
2. 新建分支 `git checkout -b feat/your-feature`
3. 提交 `git commit -m "feat: add ..."`
4. 發起 Pull Request

問題請提 Issue，建議請提 Discussion。

---

## 📄 授權

[MIT License](./LICENSE) © 2026 SARA Protocol

> 本課件可自由用於教學、企業培訓、二次創作，保留原作者信息即可。

---

## 🙏 致謝

- Stanford HAI & Fei-Fei Li 團隊的開創性綜述
- Anthropic MCP & Google A2A 社區的開放協議
- 所有 Star & Contributor

> 如果這個課件對你有幫助，請給個 ⭐ Star，這是對我們最大的支持！
