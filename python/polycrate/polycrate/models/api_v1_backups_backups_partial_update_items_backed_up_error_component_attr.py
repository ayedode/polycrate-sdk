from typing import Literal

ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponentAttr = Literal["items_backed_up"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponentAttr
] = {
    "items_backed_up",
}


def check_api_v1_backups_backups_partial_update_items_backed_up_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
