from typing import Literal

ApiV1AssistantSessionsListTurnStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_ASSISTANT_SESSIONS_LIST_TURN_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsListTurnStatusErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_assistant_sessions_list_turn_status_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsListTurnStatusErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_TURN_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_TURN_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
