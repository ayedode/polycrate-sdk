from typing import Literal

ApiV1MaintenancesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_maintenances_update_labels_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateLabelsErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
