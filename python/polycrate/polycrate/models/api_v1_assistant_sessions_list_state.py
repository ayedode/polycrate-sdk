from typing import Literal

ApiV1AssistantSessionsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ASSISTANT_SESSIONS_LIST_STATE_VALUES: set[ApiV1AssistantSessionsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_assistant_sessions_list_state(value: str) -> ApiV1AssistantSessionsListState:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_STATE_VALUES!r}")
