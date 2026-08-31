from typing import Literal

ApiV1HostsArchiveCreateProviderTypeErrorComponentAttr = Literal["provider_type"]

API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateProviderTypeErrorComponentAttr
] = {
    "provider_type",
}


def check_api_v1_hosts_archive_create_provider_type_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateProviderTypeErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
