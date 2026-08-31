from typing import Literal

ApiV1BackupsBackupsUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_BACKUPS_BACKUPS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_backups_backups_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateSloTargetErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
