from typing import Literal

ApiV1MaintenanceWindowsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_MAINTENANCE_WINDOWS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_maintenance_windows_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateTolerationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
