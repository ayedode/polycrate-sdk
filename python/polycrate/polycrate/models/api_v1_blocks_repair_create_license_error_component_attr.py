from typing import Literal

ApiV1BlocksRepairCreateLicenseErrorComponentAttr = Literal["license"]

API_V1_BLOCKS_REPAIR_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateLicenseErrorComponentAttr
] = {
    "license",
}


def check_api_v1_blocks_repair_create_license_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateLicenseErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
