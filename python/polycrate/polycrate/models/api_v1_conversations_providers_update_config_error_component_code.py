from typing import Literal

ApiV1ConversationsProvidersUpdateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_PROVIDERS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersUpdateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_providers_update_config_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersUpdateConfigErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
