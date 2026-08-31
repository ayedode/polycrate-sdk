from typing import Literal

ApiV1BackupsBackupsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_BACKUPS_BACKUPS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_backups_backups_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
