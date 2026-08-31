from typing import Literal

ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_backups_backups_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
