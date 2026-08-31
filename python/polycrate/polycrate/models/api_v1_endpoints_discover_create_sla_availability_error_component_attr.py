from typing import Literal

ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ENDPOINTS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_endpoints_discover_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
