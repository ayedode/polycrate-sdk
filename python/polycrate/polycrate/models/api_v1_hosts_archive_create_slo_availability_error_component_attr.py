from typing import Literal

ApiV1HostsArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_HOSTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_hosts_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
