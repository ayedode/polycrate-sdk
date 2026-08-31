from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_maintenances_complete_early_create_affected_pop_ids_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
