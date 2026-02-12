#  Biometrics AI Agent

AI-powered biometric device management for Claude Desktop and Claude Code.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-1.0-green)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

The Cams Biometrics MCP server enables conversational management of biometric attendance devices through Claude AI. Monitor device health, analyze transactions, troubleshoot issues, and manage your biometric fleet using natural language.

## Features

- 🔍 **Device Health Monitoring** - Real-time status checks, license validity, and online/offline detection
- 📊 **Activity Analysis** - Transaction logs, attendance metrics, and queue status
- 🔄 **Queue Management** - Reset stuck queues and recover data processing
- 📋 **Device Inventory** - Complete fleet overview with serial numbers, models, and labels
- 🔧 **Migration Tracking** - Monitor device migration status
- 🏓 **Connection Testing** - Verify server connectivity

## Installation

### Prerequisites

- Python 3.10 or higher
- Cams Biometrics API credentials ([Sign up here](https://camsbiometrics.com))

### Install via pip
```bash
pip install cams-biometrics-mcp
```

### Install from source
```bash
git clone https://github.com/camsunit/cams-mcp.git
cd cams-mcp
pip install -e .
```

## Configuration

### Claude Desktop

Add to your Claude Desktop config file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**Linux:** `~/.config/Claude/claude_desktop_config.json`
```json
{
  "mcpServers": {
    "cams-biometrics": {
      "command": "python",
      "args": ["-m", "cams_biometrics_mcp"]
    }
  }
}
```

### Getting Credentials

1. Visit [developer.camsbiometrics.com](https://developer.camsbiometrics.com)
2. Sign up or log in to your account
3. Navigate to API Credentials
4. Generate your `client_key` and `pass_code`

**Note:** You'll provide credentials when Claude calls the tools - they are not stored in the config.

## Usage Examples

Once installed, interact with your biometric devices through Claude:

### Check Connection
```
👤 User: "Test the connection to Cams server"
🤖 Claude: [Calls ping_connection] ✅ Connection to server is successful.
```

### View All Devices
```
👤 User: "Show me all my registered biometric devices"
🤖 Claude: [Calls fetch_device_inventory with your credentials]
         Here are your devices:
         • SN12345 - eSSL K30 Pro - Front Office
         • SN67890 - ZKTeco MB460 - Warehouse Entry
```

### Check Device Health
```
👤 User: "Is device SN12345 online? Check its license status"
🤖 Claude: [Calls check_device_health]
         Device SN12345 Status:
         • Status: Online ✅
         • License: Valid until 2025-12-31
         • Last sync: 2 minutes ago
         • Queue: Processing normally
```

### Analyze Activity
```
👤 User: "Show me today's attendance data for device SN12345"
🤖 Claude: [Calls analyze_device_activity]
         Today's Activity for SN12345:
         • Received: 47 transactions
         • In Queue: 2 pending
         • Pushed: 45 successful
         • Last connected: 10:23 AM
```

### Troubleshoot Issues
```
👤 User: "Device SN67890 is not syncing. What's wrong?"
🤖 Claude: [Calls check_device_health and analyze_device_activity]
         I found the issue:
         • Queue status: Stuck (12 pending)
         • Last retry: Failed at 9:15 AM
         • Webhook response: 500 error
         
         Would you like me to reset the queue?
```

### Reset Queue
```
👤 User: "Yes, reset the queue for SN67890"
🤖 Claude: [Calls reset_device_queue]
         ✅ Queue reset successful for SN67890
         Processing will resume automatically.
```

### Check Migration Status
```
👤 User: "What's the migration status of all my devices?"
🤖 Claude: [Calls migration_status with serial_number="ALL"]
         Migration Status:
         • SN12345: Completed ✅
         • SN67890: In Progress (78%)
         • SN11111: Not Started
```

## Available Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `ping_connection` | Test server connectivity | None |
| `fetch_device_inventory` | Get all registered devices | `client_key`, `pass_code` |
| `check_device_health` | Check device status & health | `client_key`, `pass_code`, `serial_number` (default: "ALL") |
| `analyze_device_activity` | View transaction logs & metrics | `client_key`, `pass_code`, `serial_number` (default: "ALL") |
| `migration_status` | Check device migration status | `client_key`, `pass_code`, `serial_number` (default: "ALL") |
| `reset_device_queue` | Restart stuck data queues | `client_key`, `pass_code`, `serial_number` (required) |

**💡 Tip:** Use `serial_number="ALL"` to query all devices at once (except for `reset_device_queue`).

## Architecture
```
┌─────────────────┐
│  Claude Desktop │
│   (User Chat)   │
└────────┬────────┘
         │ MCP Protocol
         ▼
┌─────────────────┐
│   MCP Server    │
│  (This Repo)    │
└────────┬────────┘
         │ HTTPS
         ▼
┌─────────────────┐
│ Cams Biometrics │
│   API Server    │
│ (Your Backend)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Biometric     │
│    Devices      │
└─────────────────┘
```

The MCP server acts as a bridge between Claude and your Cams Biometrics API. All business logic and data remain on your secure backend.

## Security

- ✅ Credentials are passed per-request, not stored
- ✅ All communication over HTTPS
- ✅ MCP server contains no business logic or secrets
- ✅ Backend API handles all authentication and authorization
- ⚠️ Never commit credentials to version control

## Development

### Local Setup
```bash
# Clone repository
git clone https://github.com/camsunit/cams-mcp.git
cd cams-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the MCP server (for testing)
python -m cams_biometrics_mcp
```

### Project Structure
```
src/cams_biometrics_mcp/
├── server.py                  # MCP server entry point
├── routes/
│   └── tool_routes.py        # Tool definitions (your code)
├── controllers/
│   └── handler_tool_controller.py  # API request handlers
└── config/
    └── config.py             # Configuration and logging
```

### Adding New Tools

1. Add handler function in `controllers/handler_tool_controller.py`
2. Create route definition in `routes/tool_routes.py`
3. Register route in `server.py`
4. Update documentation

## Troubleshooting

### Connection Issues
**Problem:** "Connection to server failed"

**Solutions:**
- Verify internet connectivity
- Check if `https://mcp.camsbiometrics.com` is accessible
- Use `ping_connection` tool to test
- Check firewall settings

### Authentication Errors
**Problem:** "Authentication failed" or "Invalid credentials"

**Solutions:**
- Verify your `client_key` and `pass_code` at [developer.camsbiometrics.com](https://developer.camsbiometrics.com)
- Ensure credentials haven't expired
- Check for typos in credentials
- Regenerate credentials if needed

### Device Not Found
**Problem:** "Device SN12345 not found"

**Solutions:**
- Use `fetch_device_inventory` to see all registered devices
- Verify serial number is correct (case-sensitive)
- Check if device is properly registered in your account
- Ensure device license is active

### Queue Stuck
**Problem:** "Queue is stuck" or "Data not syncing"

**Solutions:**
- Use `check_device_health` to diagnose the issue
- Check webhook endpoint availability
- Use `reset_device_queue` to restart processing
- Verify webhook returns expected HTTP status codes
- Contact support if issue persists

### Claude Not Detecting MCP Server
**Problem:** Tools not available in Claude

**Solutions:**
- Restart Claude Desktop after config changes
- Verify config file location is correct
- Check JSON syntax in config file
- Ensure Python is in system PATH
- Review Claude Desktop logs

## Support & Resources

- 📧 **Email:** contact@dheeram.org
- 🌐 **Website:** [camsbiometrics.com](https://camsbiometrics.com)
- 📖 **API Docs:** [developer.camsbiometrics.com](https://developer.camsbiometrics.com)
- 🐛 **Issues:** [GitHub Issues](https://github.com/camsunit/cams-mcp/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/camsunit/cams-mcp/discussions)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- Code follows existing style
- All tests pass
- Documentation is updated
- Commit messages are clear

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Links

- [Cams Biometrics Platform](https://camsbiometrics.com)
- [Developer Portal](https://developer.camsbiometrics.com)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Claude Desktop](https://claude.ai/download)
- [Anthropic Documentation](https://docs.anthropic.com)

## Changelog

### v1.0.0 (2025-02-06)
- Initial release
- Core tools: ping, inventory, health check, activity analysis, migration status, queue reset
- Full Claude Desktop integration
- Comprehensive documentation

**Made with ❤️ by Cams Biometrics Team**

*Transforming biometric device management through conversational AI*
