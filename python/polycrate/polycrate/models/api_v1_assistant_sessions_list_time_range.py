from typing import Literal

ApiV1AssistantSessionsListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_ASSISTANT_SESSIONS_LIST_TIME_RANGE_VALUES: set[ApiV1AssistantSessionsListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_assistant_sessions_list_time_range(value: str) -> ApiV1AssistantSessionsListTimeRange:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_TIME_RANGE_VALUES!r}")
