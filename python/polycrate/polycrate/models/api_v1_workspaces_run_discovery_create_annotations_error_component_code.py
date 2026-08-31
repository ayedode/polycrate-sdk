from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_workspaces_run_discovery_create_annotations_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateAnnotationsErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
