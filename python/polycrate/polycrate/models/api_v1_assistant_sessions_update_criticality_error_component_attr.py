from typing import Literal

ApiV1AssistantSessionsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ASSISTANT_SESSIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_assistant_sessions_update_criticality_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
