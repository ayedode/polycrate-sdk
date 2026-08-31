from typing import Literal

ApiV1CvesArchiveCreatePublishedAtErrorComponentAttr = Literal["published_at"]

API_V1_CVES_ARCHIVE_CREATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesArchiveCreatePublishedAtErrorComponentAttr
] = {
    "published_at",
}


def check_api_v1_cves_archive_create_published_at_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreatePublishedAtErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
