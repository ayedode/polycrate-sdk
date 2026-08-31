from typing import Literal

ApiV1WorkspacesDiscoverCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_WORKSPACES_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_workspaces_discover_create_criticality_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateCriticalityErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
