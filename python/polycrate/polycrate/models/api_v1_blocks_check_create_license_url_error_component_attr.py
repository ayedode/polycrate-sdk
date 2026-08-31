from typing import Literal

ApiV1BlocksCheckCreateLicenseUrlErrorComponentAttr = Literal["license_url"]

API_V1_BLOCKS_CHECK_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateLicenseUrlErrorComponentAttr
] = {
    "license_url",
}


def check_api_v1_blocks_check_create_license_url_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateLicenseUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
