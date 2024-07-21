from unittest.mock import patch

from src.utils import get_transactions_info


@patch("json.load")
@patch("builtins.open", create=True)
def test_get_transactions_info(mock_open, mock_json):
    mock_json.return_value = {"key": "value"}
    assert get_transactions_info("operation.json") == {"key": "value"}
    mock_open.assert_called_once_with("operation.json", encoding="utf-8")
