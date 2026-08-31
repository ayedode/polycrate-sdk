from typing import Literal

ApiV1AssistantSessionsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ASSISTANT_SESSIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_assistant_sessions_create_annotations_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsCreateAnnotationsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
