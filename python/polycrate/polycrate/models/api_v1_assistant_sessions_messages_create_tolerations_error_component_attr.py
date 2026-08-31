from typing import Literal

ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_assistant_sessions_messages_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
