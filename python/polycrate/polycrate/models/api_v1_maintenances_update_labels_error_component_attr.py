from typing import Literal

ApiV1MaintenancesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_MAINTENANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_maintenances_update_labels_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateLabelsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
