from typing import Literal

ApiV1CredentialsArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_credentials_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
