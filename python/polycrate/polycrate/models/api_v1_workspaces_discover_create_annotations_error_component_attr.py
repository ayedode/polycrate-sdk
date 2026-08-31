from typing import Literal

ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_WORKSPACES_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_workspaces_discover_create_annotations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateAnnotationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
