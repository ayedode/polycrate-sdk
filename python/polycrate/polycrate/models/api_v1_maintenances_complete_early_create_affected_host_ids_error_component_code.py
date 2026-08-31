from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_maintenances_complete_early_create_affected_host_ids_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
