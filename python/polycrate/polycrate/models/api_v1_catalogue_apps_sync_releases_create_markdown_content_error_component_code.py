from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_sync_releases_create_markdown_content_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
