from typing import Literal

ApiV1ConversationsProvidersListState = Literal["DEGRADED", "ERROR", "PENDING", "READY"]

API_V1_CONVERSATIONS_PROVIDERS_LIST_STATE_VALUES: set[ApiV1ConversationsProvidersListState] = {
    "DEGRADED",
    "ERROR",
    "PENDING",
    "READY",
}


def check_api_v1_conversations_providers_list_state(value: str) -> ApiV1ConversationsProvidersListState:
    if value in API_V1_CONVERSATIONS_PROVIDERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_LIST_STATE_VALUES!r}")
