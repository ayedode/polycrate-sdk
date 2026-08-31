from typing import Literal

ApiV1AssistantSessionsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ASSISTANT_SESSIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_assistant_sessions_update_kind_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsUpdateKindErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
