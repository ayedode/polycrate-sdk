from typing import Literal

ApiV1AssistantSessionsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ASSISTANT_SESSIONS_LIST_STATE_NOT_VALUES: set[ApiV1AssistantSessionsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_assistant_sessions_list_state_not(value: str) -> ApiV1AssistantSessionsListStateNot:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_STATE_NOT_VALUES!r}")
