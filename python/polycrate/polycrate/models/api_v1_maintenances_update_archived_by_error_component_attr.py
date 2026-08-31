from typing import Literal

ApiV1MaintenancesUpdateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_MAINTENANCES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_maintenances_update_archived_by_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateArchivedByErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
