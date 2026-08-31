from typing import Literal

ApiV1ConversationsProvidersCreateNameErrorComponentAttr = Literal["name"]

API_V1_CONVERSATIONS_PROVIDERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsProvidersCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_conversations_providers_create_name_error_component_attr(
    value: str,
) -> ApiV1ConversationsProvidersCreateNameErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_PROVIDERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
