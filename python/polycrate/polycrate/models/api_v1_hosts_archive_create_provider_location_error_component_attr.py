from typing import Literal

ApiV1HostsArchiveCreateProviderLocationErrorComponentAttr = Literal["provider_location"]

API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateProviderLocationErrorComponentAttr
] = {
    "provider_location",
}


def check_api_v1_hosts_archive_create_provider_location_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateProviderLocationErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
