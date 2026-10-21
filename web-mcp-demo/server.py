"""
Web-MCP Demo Server - 最小可運行範例
基於 Model Context Protocol (MCP) 2026-07-28 無狀態版
"""
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import json

app = FastAPI(title="Agent AI Knowledge MCP Server")

# 模擬知識庫 (可用 Qdrant / Pinecone 替換)
KNOWLEDGE = {
    "5_modules": "感知 Environment & Perception, 認知 Cognition (LLM/VLM), 行動 Action, 記憶 Memory, 學習 Learning",
    "mcp_vs_a2a": "MCP = USB-C 接工具數據，A2A = 網線 接智能體",
    "evolution": "Chatbot → RAG → Tool Calling → AI Agent → MCP-powered Agent"
}

@app.get("/.well-known/agent-card.json")
async def agent_card():
    """A2A 協議 Agent Card 發現機制"""
    return {
        "name": "Agent-Paper-Assistant",
        "version": "1.0.0",
        "description": "基於李飛飛論文的Agent知識助手",
        "capabilities": ["search_paper", "explain_modules", "compare_protocols"],
        "protocols": ["mcp", "a2a"],
        "endpoint": "wss://localhost:8000/mcp",
        "author": "Agent AI Guide"
    }

class ToolCall(BaseModel):
    tool: str
    query: str

@app.post("/mcp/call")
async def mcp_call(call: ToolCall):
    """MCP Tool 調用 - 無狀態"""
    if call.tool == "search_paper":
        result = {k: v for k,v in KNOWLEDGE.items() if call.query.lower() in k or call.query in v}
        return {"tool": call.tool, "result": result, "source": "arXiv:2401.03568"}
    return {"error": "tool not found"}

@app.websocket("/mcp")
async def websocket_mcp(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        msg = json.loads(data)
        # 模擬 MCP JSON-RPC 2.0
        response = {
            "jsonrpc": "2.0",
            "id": msg.get("id"),
            "result": KNOWLEDGE.get(msg.get("method"), "查無資料，試試 5_modules / mcp_vs_a2a")
        }
        await ws.send_text(json.dumps(response, ensure_ascii=False))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print("MCP Server running at http://localhost:8000")
    print("Agent Card at http://localhost:8000/.well-known/agent-card.json")
