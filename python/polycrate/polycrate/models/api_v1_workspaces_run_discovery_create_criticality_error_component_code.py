from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_run_discovery_create_criticality_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateCriticalityErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
