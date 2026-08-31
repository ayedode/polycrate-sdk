from typing import Literal

ApiV1BackupsBackupsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BACKUPS_BACKUPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_backups_backups_create_archived_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateArchivedErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
