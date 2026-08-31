from typing import Literal

ApiV1AssistantSessionsListStatus = Literal["closed", "open"]

API_V1_ASSISTANT_SESSIONS_LIST_STATUS_VALUES: set[ApiV1AssistantSessionsListStatus] = {
    "closed",
    "open",
}


def check_api_v1_assistant_sessions_list_status(value: str) -> ApiV1AssistantSessionsListStatus:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_STATUS_VALUES!r}")
