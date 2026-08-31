from typing import Literal

ApiV1AssistantSessionsListStatusErrorComponentAttr = Literal["status"]

API_V1_ASSISTANT_SESSIONS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsListStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_assistant_sessions_list_status_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsListStatusErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
