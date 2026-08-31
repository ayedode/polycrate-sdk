from typing import Literal

ApiV1PopsArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_POPS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pops_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
