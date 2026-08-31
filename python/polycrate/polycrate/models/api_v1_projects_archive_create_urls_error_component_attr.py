from typing import Literal

ApiV1ProjectsArchiveCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_PROJECTS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_projects_archive_create_urls_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateUrlsErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
