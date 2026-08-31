from typing import Literal

ApiV1BackupsBackupsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_BACKUPS_BACKUPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BackupsBackupsUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_backups_backups_update_kind_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateKindErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
