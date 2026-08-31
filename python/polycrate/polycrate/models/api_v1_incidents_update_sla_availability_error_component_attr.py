from typing import Literal

ApiV1IncidentsUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_INCIDENTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_incidents_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
