from typing import Literal

ApiV1BackupsBackupsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_BACKUPS_BACKUPS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_backups_backups_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
