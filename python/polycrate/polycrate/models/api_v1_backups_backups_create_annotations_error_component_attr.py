from typing import Literal

ApiV1BackupsBackupsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BACKUPS_BACKUPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_backups_backups_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
