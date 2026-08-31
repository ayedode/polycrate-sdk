from typing import Literal

ApiV1WorkspaceTemplatesListKindErrorComponentAttr = Literal["kind"]

API_V1_WORKSPACE_TEMPLATES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_workspace_templates_list_kind_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesListKindErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
