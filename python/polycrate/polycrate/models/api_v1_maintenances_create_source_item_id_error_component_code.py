from typing import Literal

ApiV1MaintenancesCreateSourceItemIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_MAINTENANCES_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateSourceItemIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_maintenances_create_source_item_id_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateSourceItemIdErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
