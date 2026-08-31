from typing import Literal

ApiV1ConversationsProvidersCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conversations_providers_create_kind_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersCreateKindErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
