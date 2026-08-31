from typing import Literal

ApiV1BackupsBackupsPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_backups_backups_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
