from typing import Literal

ApiV1CvesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_CVES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesArchiveCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_cves_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
