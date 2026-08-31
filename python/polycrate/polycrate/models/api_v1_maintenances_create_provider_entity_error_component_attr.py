from typing import Literal

ApiV1MaintenancesCreateProviderEntityErrorComponentAttr = Literal["provider_entity"]

API_V1_MAINTENANCES_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateProviderEntityErrorComponentAttr
] = {
    "provider_entity",
}


def check_api_v1_maintenances_create_provider_entity_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateProviderEntityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
