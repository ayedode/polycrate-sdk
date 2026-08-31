from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_archive_create_bypass_maintenance_window_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
