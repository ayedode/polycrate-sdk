from typing import Literal

ApiV1AssistantSessionsUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_ASSISTANT_SESSIONS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_assistant_sessions_update_status_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateStatusErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
