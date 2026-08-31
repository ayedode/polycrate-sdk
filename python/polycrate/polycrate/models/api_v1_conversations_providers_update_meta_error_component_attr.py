from typing import Literal

ApiV1ConversationsProvidersUpdateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_PROVIDERS_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsProvidersUpdateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_providers_update_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsProvidersUpdateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_PROVIDERS_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
