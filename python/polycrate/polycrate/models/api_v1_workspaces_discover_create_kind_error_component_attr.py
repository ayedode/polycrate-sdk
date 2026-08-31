from typing import Literal

ApiV1WorkspacesDiscoverCreateKindErrorComponentAttr = Literal["kind"]

API_V1_WORKSPACES_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_workspaces_discover_create_kind_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateKindErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
