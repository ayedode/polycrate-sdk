from typing import Literal

ApiV1ConversationsProvidersCreateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersCreateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_providers_create_config_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersCreateConfigErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
