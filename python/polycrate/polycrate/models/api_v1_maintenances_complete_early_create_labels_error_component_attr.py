from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_maintenances_complete_early_create_labels_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
