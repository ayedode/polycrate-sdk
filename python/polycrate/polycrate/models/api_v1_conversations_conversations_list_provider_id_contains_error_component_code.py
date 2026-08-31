from typing import Literal

ApiV1ConversationsConversationsListProviderIdContainsErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_CONTAINS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsListProviderIdContainsErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_conversations_conversations_list_provider_id_contains_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsListProviderIdContainsErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_CONTAINS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_CONTAINS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
