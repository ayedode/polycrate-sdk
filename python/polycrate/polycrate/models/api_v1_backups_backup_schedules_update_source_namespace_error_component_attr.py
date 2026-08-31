from typing import Literal

ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponentAttr = Literal["source_namespace"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponentAttr
] = {
    "source_namespace",
}


def check_api_v1_backups_backup_schedules_update_source_namespace_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
