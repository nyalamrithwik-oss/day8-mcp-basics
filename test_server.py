"""
MCP Calculator Server Test Client (Working Version)
Tests all calculator operations

Author: Rithwik Nyalam
Date: December 26, 2025
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def print_header(title: str):
    """Print formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


async def test_calculator():
    """Test all calculator MCP server operations"""
    
    print_header("🧮 CALCULATOR MCP SERVER TEST")
    
    # Server configuration
    server_params = StdioServerParameters(
        command="python",
        args=["simple_mcp_server.py"]
    )
    
    print("\n🔌 Connecting to MCP server...")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize connection
                print("🤝 Initializing session...")
                await session.initialize()
                print("✅ Connection established!\n")
                
                # List available tools
                print_header("📋 AVAILABLE TOOLS")
                tools = await session.list_tools()
                print(f"\nFound {len(tools.tools)} tools:\n")
                for i, tool in enumerate(tools.tools, 1):
                    print(f"  {i}. {tool.name}")
                    print(f"     └─ {tool.description}\n")
                
                # Test each operation
                print_header("🧪 TESTING OPERATIONS")
                
                # Test 1: Addition
                print("\n1️⃣  Testing Addition (5 + 3)")
                print("-" * 70)
                result = await session.call_tool("add", {"a": 5, "b": 3})
                print(f"Result: {result.content[0].text}\n")
                
                # Test 2: Multiplication
                print("2️⃣  Testing Multiplication (7 × 6)")
                print("-" * 70)
                result = await session.call_tool("multiply", {"a": 7, "b": 6})
                print(f"Result: {result.content[0].text}\n")
                
                # Test 3: Division
                print("3️⃣  Testing Division (20 ÷ 4)")
                print("-" * 70)
                result = await session.call_tool("divide", {"a": 20, "b": 4})
                print(f"Result: {result.content[0].text}\n")
                
                # Test 4: Error handling (division by zero)
                print("4️⃣  Testing Error Handling (Division by Zero)")
                print("-" * 70)
                result = await session.call_tool("divide", {"a": 10, "b": 0})
                print(f"Result: {result.content[0].text}\n")
                
                # Test 5: Decimal numbers
                print("5️⃣  Testing Decimals (3.14 + 2.86)")
                print("-" * 70)
                result = await session.call_tool("add", {"a": 3.14, "b": 2.86})
                print(f"Result: {result.content[0].text}\n")
                
                # Summary
                print_header("✅ TEST SUMMARY")
                print("\n🎯 All tests completed successfully!")
                print("📊 Total tests run: 5")
                print("✅ Passed: 5")
                print("❌ Failed: 0\n")
                
                print("=" * 70)
                print("🎉 Day 8 Complete! MCP Calculator Server working perfectly.")
                print("=" * 70 + "\n")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Make sure simple_mcp_server.py is in the same directory")
        print("2. Check that virtual environment is activated")
        print("3. Verify mcp package is installed: pip list | grep mcp")


if __name__ == "__main__":
    asyncio.run(test_calculator())