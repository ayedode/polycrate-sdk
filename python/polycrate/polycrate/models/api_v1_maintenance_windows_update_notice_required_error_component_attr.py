from typing import Literal

ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponentAttr = Literal["notice_required"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_NOTICE_REQUIRED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponentAttr
] = {
    "notice_required",
}


def check_api_v1_maintenance_windows_update_notice_required_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_NOTICE_REQUIRED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_NOTICE_REQUIRED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
