from typing import Literal

ApiV1AssistantSessionsCreateStatusErrorComponentAttr = Literal["status"]

API_V1_ASSISTANT_SESSIONS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_assistant_sessions_create_status_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateStatusErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
