from typing import Literal

ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_archive_create_markdown_content_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
