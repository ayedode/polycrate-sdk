from typing import Literal

ApiV1WorkspaceTemplatesListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_WORKSPACE_TEMPLATES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_workspace_templates_list_search_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesListSearchErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
