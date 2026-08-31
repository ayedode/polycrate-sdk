from typing import Literal

ApiV1MaintenancesListPopProviderEntityErrorComponentAttr = Literal["pop_provider_entity"]

API_V1_MAINTENANCES_LIST_POP_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesListPopProviderEntityErrorComponentAttr
] = {
    "pop_provider_entity",
}


def check_api_v1_maintenances_list_pop_provider_entity_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListPopProviderEntityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_POP_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_POP_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
