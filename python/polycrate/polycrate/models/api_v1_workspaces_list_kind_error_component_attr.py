from typing import Literal

ApiV1WorkspacesListKindErrorComponentAttr = Literal["kind"]

API_V1_WORKSPACES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_workspaces_list_kind_error_component_attr(value: str) -> ApiV1WorkspacesListKindErrorComponentAttr:
    if value in API_V1_WORKSPACES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
