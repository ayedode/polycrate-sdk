from typing import Literal

ApiV1AssistantSessionsMessagesCreateNameErrorComponentAttr = Literal["name"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_assistant_sessions_messages_create_name_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateNameErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
