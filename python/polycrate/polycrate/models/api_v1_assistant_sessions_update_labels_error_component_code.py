from typing import Literal

ApiV1AssistantSessionsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ASSISTANT_SESSIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_assistant_sessions_update_labels_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsUpdateLabelsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
