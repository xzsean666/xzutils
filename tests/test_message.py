"""
Tests for xzutils.message module.
"""

from unittest.mock import Mock, patch

import pytest

from xzutils.message import sendMessage


@patch("xzutils.message.slackMessage.requests.post")
def test_sendMessage(mock_post):
    """Test the sendMessage function."""
    # Mock the response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    # Test data
    webhook = "https://hooks.slack.com/test"
    message = "Test message"

    # Call the function
    response = sendMessage(webhook, message)

    # Assertions
    mock_post.assert_called_once_with(
        webhook, headers={"Content-type": "application/json"}, json={"text": message}
    )
    assert response == mock_response


def test_sendMessage_import():
    """Test that sendMessage can be imported directly from xzutils."""
    from xzutils import sendMessage

    assert callable(sendMessage)
