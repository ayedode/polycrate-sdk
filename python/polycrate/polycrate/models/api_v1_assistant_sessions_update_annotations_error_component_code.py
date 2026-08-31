from typing import Literal

ApiV1AssistantSessionsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ASSISTANT_SESSIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_assistant_sessions_update_annotations_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
