"""
MCP Server Entry Point

Initializes and runs the Cams Biometrics MCP server.
"""

import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

from .routes.tool_routes import (
    ping_connection_route,
    fetch_device_inventory_route,
    check_device_health_route,
    reset_device_queue_route,
    analyze_device_activity_route,
    migration_status_route
)
from .config.config import setup_logging


def create_server() -> Server:
    """Create and configure the MCP server instance."""
    server = Server("cams-biometrics")
    
    # Register all tool routes
    ping_connection_route(server)
    fetch_device_inventory_route(server)
    check_device_health_route(server)
    reset_device_queue_route(server)
    analyze_device_activity_route(server)
    migration_status_route(server)
    
    logging.info("✅ Cams Biometrics MCP Server initialized")
    logging.info("📡 All tools registered successfully")
    
    return server


async def run_server():
    """Run the MCP server with stdio transport."""
    setup_logging()
    logging.info("🚀 Starting Cams Biometrics MCP Server...")
    
    server = create_server()
    
    async with stdio_server() as (read_stream, write_stream):
        logging.info("🔌 Server connected and ready")
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


def main():
    """Main entry point for the MCP server."""
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        logging.info("🛑 Server stopped by user")
    except Exception as e:
        logging.error(f"❌ Server error: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
