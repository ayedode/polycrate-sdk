from typing import Literal

ApiV1AssistantSessionsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ASSISTANT_SESSIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_assistant_sessions_update_annotations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
