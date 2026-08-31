from typing import Literal

ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_LOADBALANCERS_REGIONS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_loadbalancers_regions_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
