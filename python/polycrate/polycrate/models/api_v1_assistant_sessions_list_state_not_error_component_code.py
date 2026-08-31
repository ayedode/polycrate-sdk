from typing import Literal

ApiV1AssistantSessionsListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_ASSISTANT_SESSIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_assistant_sessions_list_state_not_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsListStateNotErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
