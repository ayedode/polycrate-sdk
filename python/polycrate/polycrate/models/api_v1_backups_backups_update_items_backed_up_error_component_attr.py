from typing import Literal

ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponentAttr = Literal["items_backed_up"]

API_V1_BACKUPS_BACKUPS_UPDATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponentAttr
] = {
    "items_backed_up",
}


def check_api_v1_backups_backups_update_items_backed_up_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
