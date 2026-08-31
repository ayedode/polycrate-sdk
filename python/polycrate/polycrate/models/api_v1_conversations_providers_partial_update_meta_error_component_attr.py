from typing import Literal

ApiV1ConversationsProvidersPartialUpdateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_PROVIDERS_PARTIAL_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsProvidersPartialUpdateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_providers_partial_update_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsProvidersPartialUpdateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_PROVIDERS_PARTIAL_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_PARTIAL_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
