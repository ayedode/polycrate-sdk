from typing import Literal

ApiV1CatalogueAppsCreateMarkdownContentErrorComponentAttr = Literal["markdown_content"]

API_V1_CATALOGUE_APPS_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateMarkdownContentErrorComponentAttr
] = {
    "markdown_content",
}


def check_api_v1_catalogue_apps_create_markdown_content_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateMarkdownContentErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_MARKDOWN_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
