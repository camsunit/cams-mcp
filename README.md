# 🤖 Biometric AI Agent

**AI-powered biometric device management through natural conversation with Claude, ChatGPT & Gemini**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-1.0-green)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/badge/downloads-pip%20install-brightgreen)](https://pypi.org/project/cams-biometrics-mcp/)

> Transform your biometric attendance system into an intelligent AI agent. Monitor devices, analyze transactions, troubleshoot issues, and manage your entire fleet using natural language commands through Claude, ChatGPT, or Google Gemini.

**🔍  Description:** Open-source Biometric AI Agent for conversational device management. Connect Claude, ChatGPT, or Gemini to your biometric attendance fleet. Monitor health, analyze transactions, reset queues using natural language. Works with ZKTeco, eSSL, Suprema, Anviz. Free AI agent, pay only for device licenses. 150K+ devices, 100+ countries, 500M+ daily transactions.

**📱 Perfect For:** IT administrators, facility managers, security teams, HR departments, system integrators, enterprise biometric deployments, multi-location attendance tracking, partner account management

**🌐 Compatible With:** ZKTeco devices, eSSL biometric systems, Suprema readers, Anviz attendance machines, Virdi terminals, Nitgen devices, Morpho scanners, and 100+ other biometric brands worldwide

---

## 🎯 What is Biometric AI Agent?

The **Biometric AI Agent** is an intelligent assistant that connects your biometric attendance devices to AI platforms like Claude, ChatGPT, and Google Gemini. Instead of logging into dashboards and clicking through menus, simply ask questions in natural language and get instant answers about your device fleet.

**Powered by:** Model Context Protocol (MCP) + Cams Biometrics Cloud API + Your AI Assistant

**Perfect for:** IT administrators, facility managers, security teams, HR departments, and partners managing multiple client accounts.

Monitor and manage your entire biometric fleet using AI assistants like Claude, ChatGPT, or Gemini. No more dashboard hunting—just ask in natural language and get instant answers.

## 🎯 Why Use a Biometric AI Agent?

**Traditional Dashboard Approach:**  
Login → Navigate → Filter → Scroll → Check logs → Export data → Repeat  
**⏱️ Time:** ~1 hour to check 50 devices across multiple locations

**Biometric AI Agent Approach:**  
Ask AI in natural language → Get instant comprehensive answers  
**⏱️ Time:** 10 seconds  
**💡 Efficiency Gain:** 95% time savings

Managing hundreds of biometric attendance devices across multiple sites, clients, or branches used to mean endless dashboard sessions. The **Biometric AI Agent** eliminates this friction by letting you monitor everything through conversational AI—anytime, anywhere, from any device.

**Real-World Impact:**
- 🏢 **Enterprise IT Teams**: Monitor 500+ devices across 50 branches without opening a single dashboard
- 🤝 **System Integrators**: Manage multiple client accounts with simple voice commands
- 🔐 **Security Managers**: Get instant alerts about offline devices or expired licenses
- 👥 **HR Departments**: Query attendance data in real-time without technical training

📖 **Learn More:** [Next-Gen Remote Biometric Device Management Using AI Assistants](https://forum.camsbiometrics.com/next-gen-remote-biometric-device-management-using-ai-assistants/)

## ✨ Key Features of the Biometric AI Agent

Transform your biometric attendance system management with these AI-powered capabilities:

- 🔍 **Real-Time Device Monitoring** - Check online/offline status, connectivity, and health across your entire fleet
- 📊 **Intelligent Activity Analysis** - Query transaction logs, attendance metrics, and queue status with natural language
- 🔄 **Automated Queue Management** - Reset stuck queues and recover failed data syncs instantly
- 📋 **Smart Device Inventory** - Get comprehensive overviews with serial numbers, models, and custom labels
- 🔧 **Migration Status Tracking** - Monitor firmware updates and server migrations in real-time
- 🏓 **Instant Connectivity Tests** - Verify API server status with single commands
- 💬 **Natural Language Interface** - No technical training required - just ask questions normally
- 🌍 **Multi-Location Support** - Manage devices across branches, sites, and countries from one interface
- 👥 **Multi-Client Management** - Partners can handle hundreds of client accounts effortlessly
- 🔐 **Enterprise Security** - HTTPS encryption, credential rotation, zero data storage in AI agent

**SEO Keywords:** biometric AI agent, attendance system AI, biometric device management AI, conversational biometric monitoring, AI-powered attendance tracking, smart biometric fleet management, Claude biometric integration, ChatGPT attendance system, MCP biometric server

## 🚀 Quick Start - Try the Biometric AI Agent Now!

**Experience AI-powered biometric management in 5 minutes:**

### Option A: Try with Demo Account (No Setup Required!)

Get hands-on with the Biometric AI Agent immediately using our demo account:

```
Portal: https://camsbiometrics.com
Demo Login: mcpdemo
Demo Password: mcpdemo
```

**Steps:**
1. Login to the Cams Portal with demo credentials
2. Navigate to **Settings → MCP Setting → MCP Pass Key Generation**
3. Click **Generate** to create your Client Key and Passcode
4. Copy the auto-generated prompt (contains credentials)
5. Open Claude Desktop, ChatGPT, or Google Gemini with MCP support
6. Paste the prompt and start asking questions!

**Try these commands:**
- *"Show me all my biometric devices"*
- *"Which devices are currently offline?"*
- *"Check license expiration dates"*
- *"What's today's attendance transaction count?"*

**🎬 Watch the Biometric AI Agent in action:** [YouTube Demo](https://forum.camsbiometrics.com/next-gen-remote-biometric-device-management-using-ai-assistants/)

### Option B: Set Up Your Own AI Agent

For production use with your actual biometric fleet, create your free account and deploy your personal AI agent.

## 📦 Installation - Deploy Your Biometric AI Agent

### Prerequisites

To run your own Biometric AI Agent, you need:

- **Python 3.10 or higher** - [Download Python](https://www.python.org/downloads/)
- **FREE Cams Biometrics account** - Sign up at [camsbiometrics.com](https://camsbiometrics.com)
  - Demo available: `mcpdemo` / `mcpdemo`
  - Or create your own free production account
  - No charges for account creation or AI agent deployment
  - Charges only apply when adding API licenses to physical biometric devices
- **AI Assistant with MCP Support** - Claude Desktop, ChatGPT with MCP, or Google Gemini

### Install the Biometric AI Agent via pip

The fastest way to deploy your AI agent:

```bash
pip install cams-biometrics-mcp
```

### Install from Source (For Developers)

Clone and customize the Biometric AI Agent:

```bash
git clone https://github.com/camsunit/cams-mcp.git
cd cams-mcp
pip install -e .
```

## ⚙️ Configuration - Connect Your AI Assistant to the Biometric AI Agent

### For Claude Desktop

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

### For Other AI Assistants

MCP works with any Model Context Protocol-compatible AI assistant:
- **Claude Desktop** (via config above)
- **ChatGPT** (with MCP plugin)
- **Google Gemini** (with MCP adapter)
- **GitHub Copilot** (with MCP extension)

Refer to your AI assistant's MCP integration documentation for setup instructions.

### Getting Your Credentials

**Option 1: Demo Account (Quick Test)**
- Portal: https://camsbiometrics.com
- Login: `mcpdemo` / Password: `mcpdemo`
- Go to **MCP Setting → MCP Pass Key Generation**
- Copy Client Key and Passcode

**Option 2: Your Own Account**
1. Visit [camsbiometrics.com](https://camsbiometrics.com)
2. **Sign up for a FREE account** (no charges for account creation)
3. Login to your account
4. Navigate to **MCP Setting → MCP Pass Key Generation**
5. Generate your personal `client_key` and `pass_code`
6. Copy the generated prompt (includes credentials pre-filled)

**📌 Important Notes:**
- ✅ **Account creation is FREE** - No charges for signing up or using the portal
- ✅ **MCP credentials are FREE** - No cost to generate Client Key and Passcode
- 💰 **Charges apply only for API licenses** - You only pay when attaching API licenses to your physical biometric devices
- 🔑 **Credentials are per-request** - Not stored in config files, passed when Claude calls tools
- 🔓 **No auth for ping** - `ping_connection` tool works without credentials
- 🔐 **Auth required for device queries** - All device-specific tools need Client Key + Passcode

## 💡 Biometric AI Agent Usage Examples

See how natural language transforms biometric device management:

### Basic Device Monitoring with Your AI Agent

**Check Connection**
```
👤 User: "Test the Cams server connection"
🤖 Claude: [Calls ping_connection] 
         ✅ Connection to server is successful.
```

**View All Devices**
```
👤 User: "Show me all my registered devices"
🤖 Claude: [Calls fetch_device_inventory]
         You have 42 devices registered:
         • 6426163100188 - RSP10i3 - Main Office
         • CKUH202360525 - RSP10i3 - Cafeteria
         • ZYRE21025582 - Macronium (i35) - Warehouse
         [...]
```

**Check Device Status**
```
👤 User: "Is device 6426163100188 online? Check its license"
🤖 Claude: [Calls check_device_health]
         Device 6426163100188 Status:
         • Online: ❌ Offline
         • License: ✅ Valid until Feb 10, 2027
         • Queue: Processing normally
         • Last sync: 2 hours ago
```

### Advanced Monitoring

**Today's Activity**
```
👤 User: "Show today's attendance transactions for all devices"
🤖 Claude: [Calls analyze_device_activity]
         Today's Activity Summary:
         • Total Received: 247 transactions
         • In Queue: 12 pending
         • Successfully Pushed: 235
         • Failed: 0
```

**Find Issues**
```
👤 User: "Which devices have expired licenses?"
🤖 Claude: [Calls check_device_health for ALL]
         28 devices have expired licenses:
         • BXUC183060554 - CAMS 7500 (Expired)
         • ZXOL23807408 - SlimBeast (Expired)
         • SAMA05180075 - RC33 (Expired)
         [...]
         
         Would you like me to generate a renewal report?
```

### Troubleshooting & Repairs

**Diagnose Problems**
```
👤 User: "Device CKUH202360525 isn't syncing. What's wrong?"
🤖 Claude: [Calls check_device_health + analyze_device_activity]
         Found the issue:
         • Queue Status: ⚠️ Stuck (18 pending transactions)
         • Last Successful Sync: 3 hours ago
         • Error: Webhook timeout (500 error)
         
         Recommendation: Reset the queue to resume processing.
         Shall I reset it now?
```

**Fix Queue Issues**
```
👤 User: "Yes, reset the queue for CKUH202360525"
🤖 Claude: [Calls reset_device_queue]
         ✅ Queue reset successful for CKUH202360525
         Data processing will resume automatically.
         Monitoring for next sync...
```

### Multi-Client Management (For Partners)

```
👤 User: "List devices for all my clients and show which are offline"
🤖 Claude: [Calls fetch_device_inventory + check_device_health]
         Client Summary:
         
         ABC Pvt Ltd (12 devices):
         • 8 online ✅  |  4 offline ❌
         
         XYZ Corp (28 devices):
         • 24 online ✅  |  4 offline ❌
         
         Offline devices require attention:
         • ABC: SN12345, SN67890, SN11111, SN22222
         • XYZ: SN33333, SN44444, SN55555, SN66666
```

## 🛠️ Biometric AI Agent Capabilities (Available Tools)

| Tool | Description | Auth Required | Parameters |
|------|-------------|---------------|------------|
| `ping_connection` | Test server connectivity | ❌ No | None |
| `fetch_device_inventory` | Get all registered devices | ✅ Yes | `client_key`, `pass_code` |
| `check_device_health` | Check device status & health | ✅ Yes | `client_key`, `pass_code`, `serial_number*` |
| `analyze_device_activity` | View transaction logs & metrics | ✅ Yes | `client_key`, `pass_code`, `serial_number*` |
| `migration_status` | Check device migration status | ✅ Yes | `client_key`, `pass_code`, `serial_number*` |
| `reset_device_queue` | Restart stuck data queues | ✅ Yes | `client_key`, `pass_code`, `serial_number` |

**\*serial_number:** Use `"ALL"` to query all devices (default for most tools), or specify a device serial number.

**🔓 Authentication:**
- ❌ `ping_connection` - No credentials needed (test connectivity anytime)
- ✅ All other tools - Require Client Key + Passcode from [MCP Settings](https://camsbiometrics.com)

**🔒 Safety Annotations:**
- ✅ **Read-only tools** (5): Safe to call repeatedly, no state modifications
- ⚠️ **Destructive tools** (1): `reset_device_queue` modifies device state, requires confirmation

## 🏗️ Biometric AI Agent Architecture

**How your AI assistant becomes a biometric device expert:**

```
┌──────────────────────┐
│   You (Natural       │  ← "Which devices are offline?"
│   Language Query)    │     "Reset queue for SN12345"
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   AI Assistant       │  ← Claude Desktop / ChatGPT / Gemini
│ (Claude/ChatGPT/     │     Understands intent, calls tools
│      Gemini)         │
└──────────┬───────────┘
           │ MCP Protocol (Server-Sent Events)
           ▼
┌──────────────────────┐
│  Biometric AI Agent  │  ← This Repository (MCP Server)
│   (MCP Server)       │     Translates AI requests to API calls
│  Running Locally     │
└──────────┬───────────┘
           │ HTTPS API Calls (Encrypted)
           ▼
┌──────────────────────┐
│ Cams Biometrics      │  ← Cloud API Infrastructure
│   Cloud API          │     500M+ daily transactions
│  (Your Backend)      │     100+ countries, 150K+ devices
└──────────┬───────────┘
           │ Real-time Device Communication
           ▼
┌──────────────────────┐
│   Your Biometric     │  ← ZKTeco, eSSL, Suprema, Anviz
│  Attendance Devices  │     Face, Fingerprint, RFID, Iris
│   (Global Fleet)     │     Multi-location, multi-client
└──────────────────────┘
```

**How It Works:**
1. **You ask** a question in plain English to your AI assistant
2. **AI understands** your intent and determines which tool to call
3. **MCP Server** (Biometric AI Agent) receives the request locally
4. **API calls** are made securely over HTTPS to Cams Cloud
5. **Cams API** retrieves real-time data from your biometric devices
6. **Data flows back** through the chain to the AI assistant
7. **AI presents** the answer in conversational, easy-to-understand format

**Security & Privacy:**
- ✅ MCP Server runs **locally on your machine** - no cloud dependency
- ✅ No business logic or secrets stored in the AI Agent
- ✅ All communication uses **HTTPS encryption**
- ✅ Credentials passed per-request, **never persisted**
- ✅ Authentication and authorization handled by **Cams backend only**

## 🔐 Security

- ✅ **No stored credentials** - Passed per-request, never persisted
- ✅ **HTTPS only** - All API communication encrypted
- ✅ **Zero business logic** - MCP server is a stateless proxy
- ✅ **Backend authorization** - All auth handled by Cams API
- ✅ **Credential rotation** - Generate new keys anytime in portal
- ⚠️ **Never commit credentials** to version control

## 🎬 Video Tutorial - See the Biometric AI Agent in Action

Watch how the Biometric AI Agent transforms traditional device management into conversational intelligence:

[![Biometric AI Agent Demo](https://img.youtube.com/vi/RhzmKA8KZFA/0.jpg)](https://www.youtube.com/watch?v=RhzmKA8KZFA&t=2s)

**[▶️ Watch: Agentic API - The Future of Biometric API Management](https://www.youtube.com/watch?v=RhzmKA8KZFA&t=2s)**

**What you'll learn:**
- How to set up the Biometric AI Agent in under 5 minutes
- Real-time device health monitoring through natural conversation
- Troubleshooting stuck queues with simple voice commands
- Managing multi-client biometric fleets without dashboards
- Instant license expiration alerts and compliance monitoring

## 🧑‍💻 Development - Extend Your Biometric AI Agent

### Local Development Setup

Customize and enhance your Biometric AI Agent:

```bash
# Clone repository
git clone https://github.com/camsunit/cams-mcp.git
cd cams-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Run the MCP server
python -m cams_biometrics_mcp
```

### Project Structure

```
src/cams_biometrics_mcp/
├── server.py                       # MCP server entry point
├── routes/
│   └── mcp_tool_controller.py     # Tool definitions with safety annotations
├── controllers/
│   └── handler_tool_controller.py # API request handlers
└── config/
    └── config.py                  # Configuration and logging
```

### Adding New Tools

1. **Add API handler** in `controllers/handler_tool_controller.py`
2. **Create route** in `routes/mcp_tool_controller.py`
3. **Register route** in `server.py`
4. **Add safety annotation** (`readOnlyHint` or `destructiveHint`)
5. **Update documentation**

Example:
```python
def new_feature_route(mcp):
    @mcp.tool(annotations={"readOnlyHint": True})
    async def new_feature(client_key: str, pass_code: str) -> str:
        """Description of what this tool does."""
        data, client_name = await new_feature_handler(client_key, pass_code)
        return data
```

## 🐛 Troubleshooting

### Connection Issues

**Problem:** "Connection to server failed"

**Solutions:**
- ✅ Verify internet connectivity
- ✅ Test with `ping_connection` tool
- ✅ Check if `https://mcp.camsbiometrics.com` is accessible
- ✅ Review firewall/proxy settings
- ✅ Restart MCP server

### Authentication Errors

**Problem:** "Authentication failed" / "Invalid credentials"

**Solutions:**
- ✅ Verify credentials at [camsbiometrics.com](https://camsbiometrics.com) → MCP Setting
- ✅ Try demo account: `mcpdemo` / `mcpdemo`
- ✅ Check for typos in Client Key or Passcode
- ✅ Regenerate credentials if needed
- ✅ Ensure credentials haven't expired

### Device Not Found

**Problem:** "Device SN12345 not found"

**Solutions:**
- ✅ Use `fetch_device_inventory` to list all devices
- ✅ Verify serial number (case-sensitive)
- ✅ Check device is registered in your account
- ✅ Confirm device has active license

### Queue Stuck

**Problem:** "Queue is stuck" / "Data not syncing"

**Solutions:**
- ✅ Use `check_device_health` to diagnose
- ✅ Verify webhook endpoint is reachable
- ✅ Use `reset_device_queue` to restart processing
- ✅ Check webhook returns proper HTTP status codes
- ✅ Monitor device logs for recurring errors

### Claude Not Detecting Server

**Problem:** MCP tools not available in Claude

**Solutions:**
- ✅ Restart Claude Desktop after config changes
- ✅ Verify config file path is correct for your OS
- ✅ Check JSON syntax (use a JSON validator)
- ✅ Ensure Python is in system PATH
- ✅ Check Claude Desktop logs for errors
- ✅ Try removing and re-adding the MCP server config

## 📚 Resources

- 🌐 **Portal:** [camsbiometrics.com](https://camsbiometrics.com)
- 📖 **API Documentation:** [Biometric Web API](https://camsbiometrics.com/application/biometric-web-api.html)
- 📺 **Video Tutorial:** [YouTube Demo](https://www.youtube.com/watch?v=RhzmKA8KZFA&t=2s)
- 📝 **Blog Post:** [AI-Powered Device Management](https://forum.camsbiometrics.com/next-gen-remote-biometric-device-management-using-ai-assistants/)
- 🔧 **API Reference:** [Biometric Web API](https://camsbiometrics.com/application/biometric-web-api.html)
- 💬 **Support:** support@camsbiometrics.com

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open Pull Request

**Guidelines:**
- Follow existing code style (PEP 8)
- Add safety annotations to new tools
- Update documentation
- Include tests
- Write clear commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star History

If this project helps you manage your biometric fleet more efficiently, please consider giving it a star! ⭐

## 🔗 Related Resources

- [Cams Biometrics Portal](https://camsbiometrics.com) - Get your free account and MCP credentials
- [Biometric Web API Documentation](https://camsbiometrics.com/application/biometric-web-api.html) - Full API reference
- [Device Compatibility Checker](https://developer.camsbiometrics.com) - For ZKTeco, eSSL, and 3rd party device verification
- [Model Context Protocol](https://modelcontextprotocol.io) - MCP specification
- [Claude Desktop](https://claude.ai/download) - Download Claude
- [Anthropic MCP Documentation](https://docs.anthropic.com/en/docs/build-with-claude/mcp) - Build with MCP

**Note:** The Device Compatibility Checker (developer.camsbiometrics.com) is for verifying API support in ZKTeco, eSSL, and other third-party biometric devices. For MCP credentials, always use your [Cams Portal account](https://camsbiometrics.com).

## 📊 Biometric AI Agent Global Impact

**Real-World Deployment Statistics:**

- **🌍 Global Coverage:** 100+ countries worldwide
- **📱 Daily Transactions:** 500M+ attendance records processed
- **🔧 Connected Devices:** 150,000+ active biometric machines
- **👥 Enterprise Clients:** 1,000+ organizations using Cams platform
- **⏱️ Time Savings:** 95% reduction in manual dashboard management
- **🤖 AI Platforms:** Claude Desktop, ChatGPT, Google Gemini, GitHub Copilot
- **🏢 Use Cases:** Offices, factories, warehouses, hospitals, schools, retail
- **🔐 Device Brands:** ZKTeco, eSSL, Suprema, Anviz, Virdi, Nitgen, Morpho, and 100+ more

**Industry Applications:**
- 🏭 **Manufacturing:** Multi-shift attendance tracking across production floors
- 🏥 **Healthcare:** Hospital staff time management and compliance monitoring  
- 🏫 **Education:** Student and faculty attendance for multiple campuses
- 🏪 **Retail:** Chain store employee attendance and access control
- 🏗️ **Construction:** Site worker tracking across multiple project locations
- 💼 **Corporate:** Enterprise employee time and attendance management

## 💰 Pricing & Licensing - Free Biometric AI Agent, Pay Only for Devices

**The Biometric AI Agent is 100% FREE:**
- ✅ Cams Biometrics account creation - **FREE**
- ✅ AI Agent MCP server (this software) - **FREE & Open Source**
- ✅ MCP credential generation - **FREE**  
- ✅ Unlimited AI queries - **FREE**
- ✅ Portal access - **FREE**
- ✅ Multi-client management - **FREE**

**Charges Apply Only For:**
- 💵 **API License per physical biometric device** - When you attach an API license to your attendance hardware
- 💵 **Active device connectivity** - Pay only for devices you actively connect to the cloud

**How the Biometric AI Agent Pricing Works:**
1. Create **FREE** account at [camsbiometrics.com](https://camsbiometrics.com)
2. Deploy **FREE** Biometric AI Agent on your computer
3. Generate **FREE** MCP credentials (Client Key + Passcode)
4. Use the AI Agent to monitor devices at **no cost**
5. Only pay when purchasing **API licenses for physical biometric attendance machines**

**💡 Real-World Example:**  
You have 50 biometric attendance devices across 5 office locations:
- **Biometric AI Agent**: FREE ✅
- **Portal & Credentials**: FREE ✅
- **Device API Licenses**: Pay for 50 device licenses 💵
- **AI Queries**: Unlimited, FREE ✅

The AI Agent itself costs nothing - you only pay for connectivity licenses on your physical hardware.

## 📅 Changelog

### v1.0.0 (2025-02-12)
- ✅ Initial production release
- ✅ 6 core tools with safety annotations
- ✅ Full Claude Desktop integration
- ✅ Demo account support
- ✅ Comprehensive documentation
- ✅ Video tutorials and examples

---

**Built with ❤️ by the Cams Biometrics Team**

*Transforming biometric attendance device management through conversational AI agents*

**🤖 Deploy your Biometric AI Agent today:**  
Demo it now with `mcpdemo` / `mcpdemo` at [camsbiometrics.com](https://camsbiometrics.com) and experience the future of intelligent device management!

**lobehub MCP Badge:** [![MCP Badge](https://lobehub.com/badge/mcp/camsunit-cams-mcp)](https://lobehub.com/mcp/camsunit-cams-mcp)

---

**Keywords for search:** biometric ai agent, attendance system ai assistant, ai-powered biometric monitoring, conversational device management, claude biometric integration, chatgpt attendance system, mcp biometric server, intelligent fleet management, ai biometric dashboard, natural language device control, smart attendance monitoring, enterprise biometric ai
