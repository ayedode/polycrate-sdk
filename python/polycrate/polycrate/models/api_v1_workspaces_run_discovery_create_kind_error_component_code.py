from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_kind_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateKindErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
