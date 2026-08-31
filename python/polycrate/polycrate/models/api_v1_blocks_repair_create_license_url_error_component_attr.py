from typing import Literal

ApiV1BlocksRepairCreateLicenseUrlErrorComponentAttr = Literal["license_url"]

API_V1_BLOCKS_REPAIR_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateLicenseUrlErrorComponentAttr
] = {
    "license_url",
}


def check_api_v1_blocks_repair_create_license_url_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateLicenseUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
