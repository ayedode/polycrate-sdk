from typing import Literal

ApiV1BlocksCreateLicenseUrlErrorComponentAttr = Literal["license_url"]

API_V1_BLOCKS_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateLicenseUrlErrorComponentAttr] = {
    "license_url",
}


def check_api_v1_blocks_create_license_url_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateLicenseUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
