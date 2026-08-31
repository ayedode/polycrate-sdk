from typing import Literal

ApiV1MaintenancesCreateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_create_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
