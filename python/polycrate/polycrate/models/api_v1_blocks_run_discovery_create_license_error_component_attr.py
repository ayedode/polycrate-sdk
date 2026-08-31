from typing import Literal

ApiV1BlocksRunDiscoveryCreateLicenseErrorComponentAttr = Literal["license"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateLicenseErrorComponentAttr
] = {
    "license",
}


def check_api_v1_blocks_run_discovery_create_license_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateLicenseErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
