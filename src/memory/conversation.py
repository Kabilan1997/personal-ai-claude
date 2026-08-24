"""Conversation Memory Management - Maintains context across multiple turns"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

logger = logging.getLogger(__name__)


@dataclass
class Message:
    """Single message in conversation"""
    role: str  # "user" or "assistant"
    content: str
    timestamp: str

    def to_dict(self) -> Dict:
        return asdict(self)


class ConversationMemory:
    """Manages conversation history and context"""

    def __init__(self, max_messages: int = 20):
        """
        Initialize conversation memory
        
        Args:
            max_messages: Maximum messages to keep in memory
        """
        self.max_messages = max_messages
        self.messages: List[Message] = []
        self.metadata = {}

    def add_message(self, role: str, content: str) -> None:
        """Add a message to conversation history"""
        message = Message(
            role=role,
            content=content,
            timestamp=datetime.now().isoformat()
        )
        self.messages.append(message)
        
        # Keep only recent messages
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
        
        logger.debug(f"Added {role} message: {content[:50]}...")

    def get_context(self, num_messages: Optional[int] = None) -> str:
        """Get recent conversation context as formatted string"""
        messages = self.messages[-num_messages:] if num_messages else self.messages
        
        context = ""
        for msg in messages:
            context += f"{msg.role.upper()}: {msg.content}\n"
        
        return context

    def clear(self) -> None:
        """Clear all conversation history"""
        self.messages = []
        logger.info("Conversation memory cleared")

    def get_messages(self) -> List[Dict]:
        """Get all messages as list of dicts"""
        return [msg.to_dict() for msg in self.messages]

    def set_metadata(self, key: str, value: any) -> None:
        """Store metadata about the conversation"""
        self.metadata[key] = value

    def get_metadata(self, key: str, default=None):
        """Retrieve metadata"""
        return self.metadata.get(key, default)
