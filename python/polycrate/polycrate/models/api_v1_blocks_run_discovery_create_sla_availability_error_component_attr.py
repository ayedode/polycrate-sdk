from typing import Literal

ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_blocks_run_discovery_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
