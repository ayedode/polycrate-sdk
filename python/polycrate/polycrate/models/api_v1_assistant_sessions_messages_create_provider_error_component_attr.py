from typing import Literal

ApiV1AssistantSessionsMessagesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_assistant_sessions_messages_create_provider_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateProviderErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
