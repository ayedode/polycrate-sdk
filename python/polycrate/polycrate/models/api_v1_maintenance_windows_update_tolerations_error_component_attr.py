from typing import Literal

ApiV1MaintenanceWindowsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_maintenance_windows_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
