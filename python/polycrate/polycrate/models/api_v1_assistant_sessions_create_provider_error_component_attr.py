from typing import Literal

ApiV1AssistantSessionsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ASSISTANT_SESSIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_assistant_sessions_create_provider_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateProviderErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
