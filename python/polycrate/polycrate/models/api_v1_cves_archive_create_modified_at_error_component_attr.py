from typing import Literal

ApiV1CvesArchiveCreateModifiedAtErrorComponentAttr = Literal["modified_at"]

API_V1_CVES_ARCHIVE_CREATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesArchiveCreateModifiedAtErrorComponentAttr
] = {
    "modified_at",
}


def check_api_v1_cves_archive_create_modified_at_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreateModifiedAtErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
