from typing import Literal

ApiV1HostsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_HOSTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_hosts_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
