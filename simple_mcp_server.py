"""
Simple MCP Calculator Server (Working Version for mcp-1.25.0)
Day 8: MCP Fundamentals

Author: Rithwik Nyalam
Date: December 26, 2025
"""

import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from typing import Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("calculator-mcp")

# Initialize MCP server
app = Server("calculator-mcp-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """Register available calculation tools"""
    return [
        Tool(
            name="add",
            description="Add two numbers together and return the sum",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="multiply",
            description="Multiply two numbers together",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="divide",
            description="Divide first number by second number",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "Numerator"},
                    "b": {"type": "number", "description": "Denominator"}
                },
                "required": ["a", "b"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Execute the requested calculation"""
    
    try:
        if name == "add":
            a = arguments["a"]
            b = arguments["b"]
            result = a + b
            return [TextContent(
                type="text",
                text=f"✅ {a} + {b} = {result}"
            )]
        
        elif name == "multiply":
            a = arguments["a"]
            b = arguments["b"]
            result = a * b
            return [TextContent(
                type="text",
                text=f"✅ {a} × {b} = {result}"
            )]
        
        elif name == "divide":
            a = arguments["a"]
            b = arguments["b"]
            
            if b == 0:
                return [TextContent(
                    type="text",
                    text="❌ Error: Cannot divide by zero!"
                )]
            
            result = a / b
            return [TextContent(
                type="text",
                text=f"✅ {a} ÷ {b} = {result}"
            )]
        
        else:
            return [TextContent(
                type="text",
                text=f"❌ Unknown tool: {name}"
            )]
    
    except Exception as e:
        logger.error(f"❌ Error executing {name}: {str(e)}")
        return [TextContent(
            type="text",
            text=f"❌ Error: {str(e)}"
        )]


async def main():
    """Run the MCP server"""
    logger.info("🚀 Starting Calculator MCP Server...")
    logger.info("📋 Available operations: add, multiply, divide")
    logger.info("🔌 Listening on stdio for MCP connections...")
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())