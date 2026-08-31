from typing import Literal

ApiV1MaintenancesListPopProviderEntityErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_MAINTENANCES_LIST_POP_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesListPopProviderEntityErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_maintenances_list_pop_provider_entity_error_component_code(
    value: str,
) -> ApiV1MaintenancesListPopProviderEntityErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_POP_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_POP_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
