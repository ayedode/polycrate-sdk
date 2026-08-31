from typing import Literal

ApiV1ConversationsProvidersListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_CONVERSATIONS_PROVIDERS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_conversations_providers_list_state_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersListStateErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
