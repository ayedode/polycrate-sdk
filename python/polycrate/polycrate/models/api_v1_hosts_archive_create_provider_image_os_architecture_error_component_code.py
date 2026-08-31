from typing import Literal

ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_IMAGE_OS_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_archive_create_provider_image_os_architecture_error_component_code(
    value: str,
) -> ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponentCode:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_IMAGE_OS_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_PROVIDER_IMAGE_OS_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
