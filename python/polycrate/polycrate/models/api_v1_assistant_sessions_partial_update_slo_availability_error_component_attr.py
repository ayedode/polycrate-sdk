from typing import Literal

ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_assistant_sessions_partial_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsPartialUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
