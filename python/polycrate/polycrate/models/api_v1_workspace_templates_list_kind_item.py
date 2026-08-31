from typing import Literal

ApiV1WorkspaceTemplatesListKindItem = Literal["generic"]

API_V1_WORKSPACE_TEMPLATES_LIST_KIND_ITEM_VALUES: set[ApiV1WorkspaceTemplatesListKindItem] = {
    "generic",
}


def check_api_v1_workspace_templates_list_kind_item(value: str) -> ApiV1WorkspaceTemplatesListKindItem:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_KIND_ITEM_VALUES!r}")
