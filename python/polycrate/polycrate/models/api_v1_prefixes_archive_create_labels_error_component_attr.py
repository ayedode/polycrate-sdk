from typing import Literal

ApiV1PrefixesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PREFIXES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_prefixes_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
