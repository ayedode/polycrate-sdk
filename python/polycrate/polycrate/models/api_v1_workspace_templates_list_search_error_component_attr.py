from typing import Literal

ApiV1WorkspaceTemplatesListSearchErrorComponentAttr = Literal["search"]

API_V1_WORKSPACE_TEMPLATES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_workspace_templates_list_search_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesListSearchErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
