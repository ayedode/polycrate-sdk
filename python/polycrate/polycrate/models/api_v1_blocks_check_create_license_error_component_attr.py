from typing import Literal

ApiV1BlocksCheckCreateLicenseErrorComponentAttr = Literal["license"]

API_V1_BLOCKS_CHECK_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCheckCreateLicenseErrorComponentAttr] = {
    "license",
}


def check_api_v1_blocks_check_create_license_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateLicenseErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
