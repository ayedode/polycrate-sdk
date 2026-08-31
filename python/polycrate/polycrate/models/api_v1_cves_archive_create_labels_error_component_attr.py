from typing import Literal

ApiV1CvesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CVES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesArchiveCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_cves_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
