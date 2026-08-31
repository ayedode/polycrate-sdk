from typing import Literal

ApiV1AssistantSessionsListTurnStatus = Literal["idle", "queued", "running"]

API_V1_ASSISTANT_SESSIONS_LIST_TURN_STATUS_VALUES: set[ApiV1AssistantSessionsListTurnStatus] = {
    "idle",
    "queued",
    "running",
}


def check_api_v1_assistant_sessions_list_turn_status(value: str) -> ApiV1AssistantSessionsListTurnStatus:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_TURN_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_TURN_STATUS_VALUES!r}"
    )
