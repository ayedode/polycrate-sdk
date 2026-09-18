from typing import Literal

ApiV1MaintenancesListAffectedOrganizationErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_MAINTENANCES_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesListAffectedOrganizationErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_maintenances_list_affected_organization_error_component_code(
    value: str,
) -> ApiV1MaintenancesListAffectedOrganizationErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
