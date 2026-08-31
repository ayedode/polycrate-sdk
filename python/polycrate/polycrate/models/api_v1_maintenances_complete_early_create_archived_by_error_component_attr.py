from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_maintenances_complete_early_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
