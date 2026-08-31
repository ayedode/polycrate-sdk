from typing import Literal

ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_MAINTENANCES_PARTIAL_UPDATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_maintenances_partial_update_affected_host_ids_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
