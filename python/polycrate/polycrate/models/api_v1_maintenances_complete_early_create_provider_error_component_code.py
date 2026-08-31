from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_maintenances_complete_early_create_provider_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
