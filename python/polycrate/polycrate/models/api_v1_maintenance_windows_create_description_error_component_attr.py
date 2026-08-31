from typing import Literal

ApiV1MaintenanceWindowsCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_MAINTENANCE_WINDOWS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_maintenance_windows_create_description_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateDescriptionErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
