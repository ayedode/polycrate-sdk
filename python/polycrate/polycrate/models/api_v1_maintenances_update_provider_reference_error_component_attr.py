from typing import Literal

ApiV1MaintenancesUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_MAINTENANCES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_maintenances_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
