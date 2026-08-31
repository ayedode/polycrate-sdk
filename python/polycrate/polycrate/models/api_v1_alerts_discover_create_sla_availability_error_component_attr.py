from typing import Literal

ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ALERTS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_alerts_discover_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
