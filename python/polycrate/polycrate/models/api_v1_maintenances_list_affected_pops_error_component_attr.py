from typing import Literal

ApiV1MaintenancesListAffectedPopsErrorComponentAttr = Literal["affected_pops"]

API_V1_MAINTENANCES_LIST_AFFECTED_POPS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesListAffectedPopsErrorComponentAttr
] = {
    "affected_pops",
}


def check_api_v1_maintenances_list_affected_pops_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListAffectedPopsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_AFFECTED_POPS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_AFFECTED_POPS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
