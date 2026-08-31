from typing import Literal

ApiV1ConversationsProvidersCreateOrganizationErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "required"
]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersCreateOrganizationErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_conversations_providers_create_organization_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersCreateOrganizationErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
