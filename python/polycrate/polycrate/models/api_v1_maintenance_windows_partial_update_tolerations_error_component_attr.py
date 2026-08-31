from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_maintenance_windows_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
