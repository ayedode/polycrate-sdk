from typing import Literal

ApiV1ConversationsProvidersCreateConfigErrorComponentAttr = Literal["config"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsProvidersCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_conversations_providers_create_config_error_component_attr(
    value: str,
) -> ApiV1ConversationsProvidersCreateConfigErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
