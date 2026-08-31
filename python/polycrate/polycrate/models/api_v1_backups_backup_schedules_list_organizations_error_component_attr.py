from typing import Literal

ApiV1BackupsBackupSchedulesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_backups_backup_schedules_list_organizations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListOrganizationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
