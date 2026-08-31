from typing import Literal

ApiV1MaintenancesCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_MAINTENANCES_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_maintenances_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
