from typing import Literal

ApiV1CvesArchiveCreatePublishedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CVES_ARCHIVE_CREATE_PUBLISHED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesArchiveCreatePublishedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_cves_archive_create_published_at_error_component_code(
    value: str,
) -> ApiV1CvesArchiveCreatePublishedAtErrorComponentCode:
    if value in API_V1_CVES_ARCHIVE_CREATE_PUBLISHED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_PUBLISHED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
