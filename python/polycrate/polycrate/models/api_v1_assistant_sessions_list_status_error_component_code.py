from typing import Literal

ApiV1AssistantSessionsListStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_ASSISTANT_SESSIONS_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsListStatusErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_assistant_sessions_list_status_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsListStatusErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
