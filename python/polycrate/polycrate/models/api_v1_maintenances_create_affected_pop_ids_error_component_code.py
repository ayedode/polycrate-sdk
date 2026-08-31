from typing import Literal

ApiV1MaintenancesCreateAffectedPopIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_MAINTENANCES_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateAffectedPopIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_maintenances_create_affected_pop_ids_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateAffectedPopIdsErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
