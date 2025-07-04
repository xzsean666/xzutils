"""
Slack message utilities.

This module requires the 'requests' library.
Install with: uv pip install xzutils[message]
"""

try:
    import requests

    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False


def sendMessage(webhook, msg):
    """
    Send a message to Slack via webhook.

    Args:
        webhook (str): Slack webhook URL
        msg (str): Message to send

    Returns:
        requests.Response: Response from the Slack API

    Raises:
        ImportError: If requests is not installed
    """
    if not _HAS_REQUESTS:
        raise ImportError(
            "The 'requests' library is required for message functionality. "
            "Install with: uv pip install xzutils[message]"
        )

    headers = {
        "Content-type": "application/json",
    }

    json_data = {
        "text": msg,
    }

    response = requests.post(
        webhook,
        headers=headers,
        json=json_data,
    )
    return response
