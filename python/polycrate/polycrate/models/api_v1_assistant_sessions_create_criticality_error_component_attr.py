from typing import Literal

ApiV1AssistantSessionsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ASSISTANT_SESSIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_assistant_sessions_create_criticality_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateCriticalityErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
