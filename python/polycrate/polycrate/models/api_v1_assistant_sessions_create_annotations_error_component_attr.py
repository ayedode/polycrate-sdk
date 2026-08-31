from typing import Literal

ApiV1AssistantSessionsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ASSISTANT_SESSIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_assistant_sessions_create_annotations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
