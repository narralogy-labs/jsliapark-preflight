import threading
from anthropic import Anthropic
from .openport_llm import anthropic_client

_client: Anthropic | None = None
_lock = threading.Lock()


def get_client() -> Anthropic:
    """Return the shared Anthropic client, creating it thread-safely on first use."""
    global _client
    with _lock:
        if _client is None:
            _client = anthropic_client()
    return _client
