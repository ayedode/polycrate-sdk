from typing import Literal

ApiV1MaintenancesPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_maintenances_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
