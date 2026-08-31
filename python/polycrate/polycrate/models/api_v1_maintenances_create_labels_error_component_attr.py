from typing import Literal

ApiV1MaintenancesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_MAINTENANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_maintenances_create_labels_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateLabelsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
