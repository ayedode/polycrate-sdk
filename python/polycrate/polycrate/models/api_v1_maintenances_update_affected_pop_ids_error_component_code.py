from typing import Literal

ApiV1MaintenancesUpdateAffectedPopIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_MAINTENANCES_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesUpdateAffectedPopIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_maintenances_update_affected_pop_ids_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateAffectedPopIdsErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
