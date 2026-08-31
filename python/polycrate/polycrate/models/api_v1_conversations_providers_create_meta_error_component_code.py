from typing import Literal

ApiV1ConversationsProvidersCreateMetaErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersCreateMetaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_providers_create_meta_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersCreateMetaErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
