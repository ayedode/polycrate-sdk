from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_workspaces_run_discovery_create_annotations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
