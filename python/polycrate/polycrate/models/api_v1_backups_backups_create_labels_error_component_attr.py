from typing import Literal

ApiV1BackupsBackupsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BACKUPS_BACKUPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_backups_backups_create_labels_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateLabelsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
