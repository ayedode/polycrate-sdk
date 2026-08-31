from typing import Literal

ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_partial_update_markdown_content_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MARKDOWN_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
