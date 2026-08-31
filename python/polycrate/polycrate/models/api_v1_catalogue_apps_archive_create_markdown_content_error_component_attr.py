from typing import Literal

ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponentAttr = Literal["markdown_content"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponentAttr
] = {
    "markdown_content",
}


def check_api_v1_catalogue_apps_archive_create_markdown_content_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
