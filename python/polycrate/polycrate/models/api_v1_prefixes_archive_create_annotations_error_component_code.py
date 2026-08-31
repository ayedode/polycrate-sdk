from typing import Literal

ApiV1PrefixesArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PREFIXES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_prefixes_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1PrefixesArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
