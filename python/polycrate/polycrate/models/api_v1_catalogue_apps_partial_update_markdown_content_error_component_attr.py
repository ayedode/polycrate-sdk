from typing import Literal

ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponentAttr = Literal["markdown_content"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponentAttr
] = {
    "markdown_content",
}


def check_api_v1_catalogue_apps_partial_update_markdown_content_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
