from typing import Literal

ApiV1HostsUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_HOSTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_hosts_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
