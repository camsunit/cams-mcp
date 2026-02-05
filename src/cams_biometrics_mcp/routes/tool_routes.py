"""
Tool Route Definitions

Defines all MCP tools for biometric device management.
"""

import json
import logging
from ..config.config import check_and_rotate_log
from ..controllers.handler_tool_controller import (
    fetch_device_inventory_handler,
    check_device_health_handler,
    reset_device_queue_handler,
    analyze_device_activity_handler,
    migration_status_handler
)


def ping_connection_route(mcp):
    """Register ping connection tool."""
    
    @mcp.tool()
    async def ping_connection() -> str:
        """
        Check the connection for server is connectable

        Returns:
            If connection is `successful`, returns a success message.
        """
        check_and_rotate_log()
        logging.info("🔍 ping_connection called")
        
        return "Connection to server is successful."


def fetch_device_inventory_route(mcp):
    """Register fetch device inventory tool."""
    
    @mcp.tool()
    async def fetch_device_inventory(client_key: str, pass_code: str) -> str:
        """
        Retrieves complete biometric device inventory for the authenticated user.

        Returns device information including serial numbers, models, custom labels,
        and associated client names (for partner accounts).

        Args:
            client_key: Client authentication key
            pass_code: User authentication passcode

        Returns:
            Formatted string containing device inventory details
        """
        check_and_rotate_log()
        logging.info("🔍 fetch_device_inventory tool called")

        try:
            data, client_name = await fetch_device_inventory_handler(client_key, pass_code)
            if not data:
                return json.dumps({"error": "Unable to fetch machine list"})

            logging.info(f"{client_name} - {data}")
            return data
        except Exception as e:
            logging.exception("Error in fetch_device_inventory")
            return json.dumps({"error": f"Failed to fetch machine list: {str(e)}"})


def check_device_health_route(mcp):
    """Register check device health tool."""
    
    @mcp.tool()
    async def check_device_health(client_key: str,
                                  pass_code: str,
                                  serial_number: str = "ALL") -> str:
        """
        Gets comprehensive status information for biometric devices.

        Returns:
            - Serial number, model, label name, client name
            - License validity (valid/expired date)
            - Associated service connections
            - Online/offline status
            - Data synchronization direction
            - Queue processing status

        Args:
            client_key: Client authentication key
            pass_code: User authentication passcode
            serial_number: Device serial number or 'ALL' for all devices

        Returns:
            Formatted string with device health details
        """
        check_and_rotate_log()
        logging.info(f"🔍 check_device_health tool called for: {serial_number}")
        
        try:
            data, client_name = await check_device_health_handler(client_key, pass_code, serial_number)
            if not data:
                return json.dumps({"error": "Unable to fetch machine status details"})

            logging.info(f"{client_name} - {data}")
            return data
        except Exception as e:
            logging.exception(f"Error in machine status details: {str(e)}")
            return json.dumps({"error": f"Failed to check device health: {str(e)}"})


def reset_device_queue_route(mcp):
    """Register reset device queue tool."""
    
    @mcp.tool()
    async def reset_device_queue(client_key: str, 
                                 pass_code: str,
                                 serial_number: str) -> str:
        """
        Restarts the data processing queue for a specific biometric device.

        Use this function when a device's queue is stuck or needs to be reset
        to resume normal data processing operations. Always check the device
        health first to get the reason for the queue being stuck.

        Args:
            client_key: Client authentication key
            pass_code: User authentication passcode
            serial_number: Serial number of the target device

        Returns:
            Status message indicating queue restart result
        """
        check_and_rotate_log()
        logging.info(f"🔍 reset_device_queue tool called for: {serial_number}")
        
        try:
            data, client_name = await reset_device_queue_handler(client_key, pass_code, serial_number)

            if not data:
                return "Unable to restart the queue of this serial number."

            logging.info(f"{client_name} - {data}")
            return data
        except Exception as e:
            logging.exception(f"Error in reset_device_queue: {str(e)}")
            return json.dumps({"error": f"Failed to reset queue: {str(e)}"})


def analyze_device_activity_route(mcp):
    """Register analyze device activity tool."""
    
    @mcp.tool()
    async def analyze_device_activity(client_key: str, 
                                      pass_code: str,
                                      serial_number: str = "ALL") -> str:
        """
        Retrieves detailed transaction logs and activity metrics for a biometric device.

        Returns comprehensive activity data including:
        - Today's attendance counts: Received, Queue, Pushed
        - Last connected time
        - Queue status and next retry time
        - Last request sent
        - Last response received
        - Connected server callback URL

        Args:
            client_key: Client Key of the user
            pass_code: Pass code of the user
            serial_number: Serial number of the machine

        Returns:
            Formatted string with device transaction details and metrics
        """
        check_and_rotate_log()
        logging.info(f"🔍 analyze_device_activity tool called for: {serial_number}")

        try:
            data, client_name = await analyze_device_activity_handler(client_key, pass_code, serial_number)

            if not data:
                return "Unable to fetch machine transaction list."

            logging.info(f"{client_name} - {data}")
            return data
        except Exception as e:
            logging.exception(f"Error in analyze_device_activity: {str(e)}")
            return json.dumps({"error": f"Failed to analyze activity: {str(e)}"})


def migration_status_route(mcp):
    """Register migration status tool."""
    
    @mcp.tool()
    async def migration_status(client_key: str, 
                              pass_code: str,
                              serial_number: str = "ALL") -> str:
        """
        Retrieves migration status for biometric devices.
        
        Args:
            client_key: Client Key of the user
            pass_code: Pass code of the user
            serial_number: Serial number of the machine
            
        Returns:
            Formatted string with device migration status details
        """
        check_and_rotate_log()
        logging.info(f"🔍 migration_status tool called for: {serial_number}")

        try:
            data, client_name = await migration_status_handler(client_key, pass_code, serial_number)
            logging.info(f"{client_name} - migration_status: {data}")
            
            if not data:
                return "Unable to fetch machine migration status."

            return data
        except Exception as e:
            logging.exception(f"Error in migration_status: {str(e)}")
            return json.dumps({"error": f"Failed to fetch migration status: {str(e)}"})
