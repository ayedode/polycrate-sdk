from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_maintenance_windows_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
