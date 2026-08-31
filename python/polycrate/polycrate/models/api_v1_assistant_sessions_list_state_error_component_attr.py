from typing import Literal

ApiV1AssistantSessionsListStateErrorComponentAttr = Literal["state"]

API_V1_ASSISTANT_SESSIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_assistant_sessions_list_state_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsListStateErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
