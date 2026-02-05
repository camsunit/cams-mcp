"""
API Handler Controllers

Handles communication with Cams Biometrics backend API.
"""

import httpx
import logging
from typing import Tuple, Optional
from ..config.config import API_URL, API_TIMEOUT


async def fetch_device_inventory_handler(
    client_key: str, 
    pass_code: str
) -> Tuple[Optional[str], str]:
    """
    Fetch device inventory from API.
    
    Args:
        client_key: Client authentication key
        pass_code: User authentication passcode
        
    Returns:
        Tuple of (data, client_name)
    """
    try:
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            response = await client.post(
                f"{API_URL}/inventory",
                json={"client_key": client_key, "pass_code": pass_code}
            )
            response.raise_for_status()
            result = response.json()
            return result.get("data"), result.get("client_name", "Unknown")
    except Exception as e:
        logging.error(f"API error in fetch_device_inventory_handler: {e}")
        return None, "Error"


async def check_device_health_handler(
    client_key: str, 
    pass_code: str, 
    serial_number: str
) -> Tuple[Optional[str], str]:
    """
    Check device health from API.
    
    Args:
        client_key: Client authentication key
        pass_code: User authentication passcode
        serial_number: Device serial number
        
    Returns:
        Tuple of (data, client_name)
    """
    try:
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            response = await client.post(
                f"{API_URL}/health",
                json={
                    "client_key": client_key,
                    "pass_code": pass_code,
                    "serial_number": serial_number
                }
            )
            response.raise_for_status()
            result = response.json()
            return result.get("data"), result.get("client_name", "Unknown")
    except Exception as e:
        logging.error(f"API error in check_device_health_handler: {e}")
        return None, "Error"


async def reset_device_queue_handler(
    client_key: str, 
    pass_code: str, 
    serial_number: str
) -> Tuple[Optional[str], str]:
    """
    Reset device queue via API.
    
    Args:
        client_key: Client authentication key
        pass_code: User authentication passcode
        serial_number: Device serial number
        
    Returns:
        Tuple of (data, client_name)
    """
    try:
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            response = await client.post(
                f"{API_URL}/queue/reset",
                json={
                    "client_key": client_key,
                    "pass_code": pass_code,
                    "serial_number": serial_number
                }
            )
            response.raise_for_status()
            result = response.json()
            return result.get("data"), result.get("client_name", "Unknown")
    except Exception as e:
        logging.error(f"API error in reset_device_queue_handler: {e}")
        return None, "Error"


async def analyze_device_activity_handler(
    client_key: str, 
    pass_code: str, 
    serial_number: str
) -> Tuple[Optional[str], str]:
    """
    Analyze device activity via API.
    
    Args:
        client_key: Client authentication key
        pass_code: User authentication passcode
        serial_number: Device serial number
        
    Returns:
        Tuple of (data, client_name)
    """
    try:
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            response = await client.post(
                f"{API_URL}/activity",
                json={
                    "client_key": client_key,
                    "pass_code": pass_code,
                    "serial_number": serial_number
                }
            )
            response.raise_for_status()
            result = response.json()
            return result.get("data"), result.get("client_name", "Unknown")
    except Exception as e:
        logging.error(f"API error in analyze_device_activity_handler: {e}")
        return None, "Error"


async def migration_status_handler(
    client_key: str, 
    pass_code: str, 
    serial_number: str
) -> Tuple[Optional[str], str]:
    """
    Get migration status via API.
    
    Args:
        client_key: Client authentication key
        pass_code: User authentication passcode
        serial_number: Device serial number
        
    Returns:
        Tuple of (data, client_name)
    """
    try:
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            response = await client.post(
                f"{API_URL}/migration",
                json={
                    "client_key": client_key,
                    "pass_code": pass_code,
                    "serial_number": serial_number
                }
            )
            response.raise_for_status()
            result = response.json()
            return result.get("data"), result.get("client_name", "Unknown")
    except Exception as e:
        logging.error(f"API error in migration_status_handler: {e}")
        return None, "Error"
