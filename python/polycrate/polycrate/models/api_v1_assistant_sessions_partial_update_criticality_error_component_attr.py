from typing import Literal

ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_assistant_sessions_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
