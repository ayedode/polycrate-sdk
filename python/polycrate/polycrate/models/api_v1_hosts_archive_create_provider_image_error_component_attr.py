from typing import Literal

ApiV1HostsArchiveCreateProviderImageErrorComponentAttr = Literal["provider_image"]

API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_IMAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateProviderImageErrorComponentAttr
] = {
    "provider_image",
}


def check_api_v1_hosts_archive_create_provider_image_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateProviderImageErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_IMAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_IMAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
