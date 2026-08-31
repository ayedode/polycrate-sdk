from typing import Literal

ApiV1MaintenancesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_MAINTENANCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_maintenances_update_annotations_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
