from typing import Literal

ApiV1BackupsBackupsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BACKUPS_BACKUPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_backups_backups_update_labels_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateLabelsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
