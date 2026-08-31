from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_maintenances_complete_early_create_archived_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
