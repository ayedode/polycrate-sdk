from typing import Literal

ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_INCIDENTS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_incidents_partial_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
