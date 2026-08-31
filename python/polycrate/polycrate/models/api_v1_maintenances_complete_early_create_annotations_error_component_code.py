from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_maintenances_complete_early_create_annotations_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
