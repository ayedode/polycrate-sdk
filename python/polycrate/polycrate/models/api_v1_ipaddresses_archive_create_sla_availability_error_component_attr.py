from typing import Literal

ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_ipaddresses_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
