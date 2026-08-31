from typing import Literal

ApiV1PopsListAffectedMaintenancesErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_POPS_LIST_AFFECTED_MAINTENANCES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsListAffectedMaintenancesErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_pops_list_affected_maintenances_error_component_code(
    value: str,
) -> ApiV1PopsListAffectedMaintenancesErrorComponentCode:
    if value in API_V1_POPS_LIST_AFFECTED_MAINTENANCES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_AFFECTED_MAINTENANCES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
