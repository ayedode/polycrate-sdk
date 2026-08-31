from typing import Literal

ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_REPAIR_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_repair_create_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
