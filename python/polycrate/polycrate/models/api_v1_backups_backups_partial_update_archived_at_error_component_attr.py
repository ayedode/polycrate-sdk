from typing import Literal

ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_backups_backups_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
