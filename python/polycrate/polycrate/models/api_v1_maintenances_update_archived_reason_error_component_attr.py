from typing import Literal

ApiV1MaintenancesUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_MAINTENANCES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_maintenances_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
