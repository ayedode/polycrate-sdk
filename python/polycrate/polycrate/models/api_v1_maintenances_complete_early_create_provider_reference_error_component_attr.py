from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_maintenances_complete_early_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
