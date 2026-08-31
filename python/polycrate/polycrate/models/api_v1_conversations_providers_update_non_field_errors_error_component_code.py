from typing import Literal

ApiV1ConversationsProvidersUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_PROVIDERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_providers_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
