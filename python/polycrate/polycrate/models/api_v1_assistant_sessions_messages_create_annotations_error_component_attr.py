from typing import Literal

ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_assistant_sessions_messages_create_annotations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
