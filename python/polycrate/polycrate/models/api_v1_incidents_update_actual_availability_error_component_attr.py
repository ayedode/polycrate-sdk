from typing import Literal

ApiV1IncidentsUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_INCIDENTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_incidents_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
