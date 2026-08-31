from typing import Literal

ApiV1NotesArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_NOTES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_notes_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
