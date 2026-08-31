from typing import Literal

ApiV1IpaddressesCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_IPADDRESSES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_ipaddresses_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
