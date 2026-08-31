from typing import Literal

ApiV1ConversationsProvidersCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsProvidersCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_conversations_providers_create_credential_error_component_attr(
    value: str,
) -> ApiV1ConversationsProvidersCreateCredentialErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
