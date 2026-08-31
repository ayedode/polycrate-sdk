from typing import Literal

ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_conversations_providers_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
