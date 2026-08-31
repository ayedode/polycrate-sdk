from typing import Literal

ApiV1NotesArchiveCreateVydeoEnabledErrorComponentAttr = Literal["vydeo_enabled"]

API_V1_NOTES_ARCHIVE_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateVydeoEnabledErrorComponentAttr
] = {
    "vydeo_enabled",
}


def check_api_v1_notes_archive_create_vydeo_enabled_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateVydeoEnabledErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_VYDEO_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
