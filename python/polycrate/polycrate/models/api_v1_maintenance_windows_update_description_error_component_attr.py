from typing import Literal

ApiV1MaintenanceWindowsUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_maintenance_windows_update_description_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateDescriptionErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
