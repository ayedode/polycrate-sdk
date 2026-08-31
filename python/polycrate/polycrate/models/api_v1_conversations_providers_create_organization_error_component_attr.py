from typing import Literal

ApiV1ConversationsProvidersCreateOrganizationErrorComponentAttr = Literal["organization"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsProvidersCreateOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_conversations_providers_create_organization_error_component_attr(
    value: str,
) -> ApiV1ConversationsProvidersCreateOrganizationErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
