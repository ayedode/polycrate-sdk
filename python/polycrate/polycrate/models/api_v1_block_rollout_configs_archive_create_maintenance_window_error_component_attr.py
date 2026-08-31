from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponentAttr = Literal["maintenance_window"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponentAttr
] = {
    "maintenance_window",
}


def check_api_v1_block_rollout_configs_archive_create_maintenance_window_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
