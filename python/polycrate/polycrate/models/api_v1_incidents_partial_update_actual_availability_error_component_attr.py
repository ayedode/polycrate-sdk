from typing import Literal

ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_INCIDENTS_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_incidents_partial_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
