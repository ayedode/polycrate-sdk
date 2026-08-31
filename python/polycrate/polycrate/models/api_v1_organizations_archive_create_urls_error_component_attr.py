from typing import Literal

ApiV1OrganizationsArchiveCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_organizations_archive_create_urls_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateUrlsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
