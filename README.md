# 🧮 Day 8: MCP Calculator Server

> **Learn Model Context Protocol fundamentals by building a calculator that Claude can use**

**Week 2, Day 8** of 30-Day RAG Learning Journey

Built by [Rithwik Nyalam](https://github.com/nyalamrithwik-oss)

---

## 🎯 Project Overview

This is your first MCP (Model Context Protocol) server! It's a calculator that exposes 5 mathematical operations as tools that Claude Desktop (or any MCP host) can use.

### What You'll Learn

✅ **MCP Architecture**: Client-server communication via stdio  
✅ **Tool Registration**: How to define tools for AI  
✅ **Tool Execution**: Handling AI requests  
✅ **Async Python**: Using asyncio for MCP servers  
✅ **Error Handling**: Graceful failures (division by zero)

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.10+
```

### Installation

1. **Navigate to Day 8 folder**

```bash
cd ~/OneDrive/RAG/week2-mcp/day8-mcp-basics/
```

2. **Create virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Running Tests

```bash
python test_server.py
```

### Expected Output

```
======================================================================
  🧮 CALCULATOR MCP SERVER TEST
======================================================================

🔌 Connecting to MCP server...
🤝 Initializing session...
✅ Connection established!

======================================================================
  📋 AVAILABLE TOOLS
======================================================================

Found 5 tools:

  1. add
     └─ Add two numbers together and return the sum

  2. subtract
     └─ Subtract second number from first number

  3. multiply
     └─ Multiply two numbers together

  4. divide
     └─ Divide first number by second number

  5. power
     └─ Raise first number to the power of second number

======================================================================
  🧪 TESTING OPERATIONS
======================================================================

1️⃣  Testing Addition (5 + 3)
----------------------------------------------------------------------
Result: ✅ 5 + 3 = 8

2️⃣  Testing Subtraction (10 - 4)
----------------------------------------------------------------------
Result: ✅ 10 - 4 = 6

...

======================================================================
  ✅ TEST SUMMARY
======================================================================

🎯 All tests completed successfully!
📊 Total tests run: 8
✅ Passed: 8
❌ Failed: 0

======================================================================
🎉 Day 8 Complete! MCP Calculator Server working perfectly.
======================================================================
```

---

## 📁 Project Structure

```
day8-mcp-basics/
├── simple_mcp_server.py    # Main MCP calculator server
├── test_server.py           # Comprehensive test client
├── requirements.txt         # Dependencies
├── .env.example            # Environment variable template
├── DAY8_NOTES.md          # Learning notes & concepts
└── README.md              # This file
```

---

## 🏗️ Architecture

### MCP Flow

```
Claude Desktop → stdio → simple_mcp_server.py → Calculation → Result
                                 ↓
                         Tool Registration
                         - add
                         - subtract
                         - multiply
                         - divide
                         - power
```

### Code Structure

```python
# 1. Tool Registration
@app.list_tools()
async def list_tools() -> List[Tool]:
    # Defines what tools are available
    return [Tool(name="add", ...)]

# 2. Tool Execution
@app.call_tool()
async def call_tool(name: str, arguments: Any):
    # Handles the actual calculations
    if name == "add":
        return result

# 3. Server Runtime
async def main():
    # Runs the stdio server
    async with stdio_server() as (read, write):
        await app.run(...)
```

---

## 🔧 Available Tools

### 1. **add**
- **Description**: Add two numbers together
- **Parameters**: `a` (number), `b` (number)
- **Example**: `add(5, 3)` → `8`

### 2. **subtract**
- **Description**: Subtract second number from first
- **Parameters**: `a` (number), `b` (number)
- **Example**: `subtract(10, 4)` → `6`

### 3. **multiply**
- **Description**: Multiply two numbers
- **Parameters**: `a` (number), `b` (number)
- **Example**: `multiply(7, 6)` → `42`

### 4. **divide**
- **Description**: Divide first number by second
- **Parameters**: `a` (numerator), `b` (denominator)
- **Example**: `divide(20, 4)` → `5`
- **Error handling**: Returns error if `b = 0`

### 5. **power**
- **Description**: Raise first number to power of second
- **Parameters**: `base` (number), `exponent` (number)
- **Example**: `power(2, 8)` → `256`

---

## 📚 Key Concepts

### What is MCP?

**Model Context Protocol (MCP)** is Anthropic's open standard for connecting AI systems to external tools and data.

**Think of it as:** USB ports for AI - a universal way to plug in tools.

### Why MCP Matters

**Without MCP (Week 1):**
```
RAG System → Static documents only
```

**With MCP (Week 2):**
```
RAG System → Static docs + Live APIs + Databases + Tools
```

### MCP vs Traditional APIs

| Feature | Traditional API | MCP |
|---------|----------------|-----|
| Built for | Developers | AI Systems |
| Discovery | Documentation | Dynamic |
| Integration | Custom code per API | Standard protocol |
| Claude support | Requires wrapper | Native |

---

## 🎓 Learning Outcomes

After completing Day 8, you should understand:

✅ **MCP Architecture**
- Client-server model
- Stdio transport protocol
- Tool registration and execution

✅ **Python Async**
- `async def` functions
- `await` keyword
- `async with` context managers

✅ **Tool Design**
- Clear descriptions for AI
- JSON Schema for validation
- Error handling patterns

✅ **MCP + RAG Connection**
- How MCP enhances RAG systems
- Why dynamic data access matters
- Planning for Portfolio Project #2

---

## 🚧 Troubleshooting

### Error: "No module named 'mcp'"

```bash
pip install mcp
```

### Error: "asyncio.run() got an unexpected keyword argument"

- Check Python version: `python --version`
- Need Python 3.10+

### Server not responding

- Make sure `simple_mcp_server.py` is in the same directory
- Check that virtual environment is activated
- Try running server directly: `python simple_mcp_server.py`

---

## 🎯 Next Steps

### Tomorrow (Day 9):

1. **Connect to Claude Desktop**
   - Configure `claude_desktop_config.json`
   - Use calculator in real Claude interface

2. **Build Database MCP Server**
   - SQLite integration
   - CRUD operations

3. **Advanced MCP Patterns**
   - Multi-tool workflows
   - Resource management

---

## 📊 Stats

- **Time to complete**: ~4 hours
- **Lines of code**: 150
- **Tools created**: 5
- **Tests passing**: 8/8 ✅
- **Concepts learned**: 10+

---

## 🔗 Resources

### Official Documentation
- [MCP Docs](https://modelcontextprotocol.io/)
- [Anthropic MCP Blog](https://www.anthropic.com/news/model-context-protocol)
- [MCP GitHub](https://github.com/modelcontextprotocol)

### Example Servers
- [Filesystem Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
- [GitHub Server](https://github.com/modelcontextprotocol/servers/tree/main/src/github)

---

## 💡 Pro Tips

1. **Clear tool descriptions**: Claude uses them to decide WHEN to use tools
2. **Handle edge cases**: Always validate inputs (like division by zero)
3. **Use emojis**: Makes console output easier to read
4. **Test thoroughly**: Write tests before connecting to Claude Desktop

---

## ✅ Completion Checklist

- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Run test client (`python test_server.py`)
- [ ] Verify all 8 tests pass
- [ ] Read `DAY8_NOTES.md` for concepts
- [ ] Take screenshots of successful tests
- [ ] Update Notion tracker
- [ ] (Optional) Post on LinkedIn

---

## 🎉 Success Criteria

You've completed Day 8 when:

✅ Test client shows all operations working  
✅ Error handling works (division by zero)  
✅ You understand MCP client-server model  
✅ You can explain the difference between MCP and traditional APIs  
✅ You're ready to build more complex MCP servers

---

## 👤 Author

**Rithwik Nyalam**

- GitHub: [@nyalamrithwik-oss](https://github.com/nyalamrithwik-oss)
- Part of: 30-Day RAG Learning Journey
- Week: 2/4
- Day: 8/30

---

## 📝 Notes

This calculator server is intentionally simple to teach fundamentals. Tomorrow (Day 9), you'll build:
- Database MCP server (more complex)
- Claude Desktop integration
- Multi-tool workflows

**Remember**: Week 1 taught you RAG. Week 2 teaches you how to make RAG systems dynamic with MCP!

---

**Day 8 Status:** ✅ Complete  
**Next:** Day 9 - Advanced MCP + Claude Desktop  
**Target:** Portfolio Project #2 by Day 13

---

_Built with ❤️ as part of the journey to $3K-5K revenue in 30 days_