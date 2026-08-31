from typing import Literal

ApiV1MaintenancesListAffectedPopsErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_MAINTENANCES_LIST_AFFECTED_POPS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesListAffectedPopsErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_maintenances_list_affected_pops_error_component_code(
    value: str,
) -> ApiV1MaintenancesListAffectedPopsErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_AFFECTED_POPS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_AFFECTED_POPS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
