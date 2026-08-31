from typing import Literal

ApiV1BlocksUpdateLicenseErrorComponentAttr = Literal["license"]

API_V1_BLOCKS_UPDATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateLicenseErrorComponentAttr] = {
    "license",
}


def check_api_v1_blocks_update_license_error_component_attr(value: str) -> ApiV1BlocksUpdateLicenseErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
