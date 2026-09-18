from typing import Literal

ApiV1MaintenancesListAffectedOrganizationErrorComponentAttr = Literal["affected_organization"]

API_V1_MAINTENANCES_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesListAffectedOrganizationErrorComponentAttr
] = {
    "affected_organization",
}


def check_api_v1_maintenances_list_affected_organization_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListAffectedOrganizationErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
