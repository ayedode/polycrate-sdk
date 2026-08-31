from typing import Literal

ApiV1BlocksArchiveCreateLicenseUrlErrorComponentAttr = Literal["license_url"]

API_V1_BLOCKS_ARCHIVE_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateLicenseUrlErrorComponentAttr
] = {
    "license_url",
}


def check_api_v1_blocks_archive_create_license_url_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateLicenseUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
