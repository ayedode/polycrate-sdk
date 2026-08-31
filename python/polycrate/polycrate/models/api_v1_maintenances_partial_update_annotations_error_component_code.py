from typing import Literal

ApiV1MaintenancesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_maintenances_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
