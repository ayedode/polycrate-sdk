from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_workspaces_run_discovery_create_labels_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateLabelsErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
