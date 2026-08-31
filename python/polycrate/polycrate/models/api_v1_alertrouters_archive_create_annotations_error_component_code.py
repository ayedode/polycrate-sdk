from typing import Literal

ApiV1AlertroutersArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertrouters_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1AlertroutersArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
