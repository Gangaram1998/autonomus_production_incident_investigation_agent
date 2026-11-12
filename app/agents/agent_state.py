from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgentState:
    user_query:str
    status: str = "pending"
    messages: list[dict[str,Any]]= field(default_factory=list)
    tool_response: list[dict[str,Any]]= field(default_factory=list)
    iterations:int = 0
    final_response: str | None = None
    error : str | None = None
