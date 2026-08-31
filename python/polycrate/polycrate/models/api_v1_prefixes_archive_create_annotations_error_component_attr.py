from typing import Literal

ApiV1PrefixesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PREFIXES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_prefixes_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
