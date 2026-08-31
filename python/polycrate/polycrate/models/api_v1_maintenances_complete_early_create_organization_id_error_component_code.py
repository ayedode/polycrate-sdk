from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_maintenances_complete_early_create_organization_id_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
