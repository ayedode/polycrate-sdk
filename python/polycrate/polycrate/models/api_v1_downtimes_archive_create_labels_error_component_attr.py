from typing import Literal

ApiV1DowntimesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_downtimes_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1DowntimesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
