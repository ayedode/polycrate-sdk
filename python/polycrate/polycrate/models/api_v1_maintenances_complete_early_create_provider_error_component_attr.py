from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_maintenances_complete_early_create_provider_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
