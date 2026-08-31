from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_on_premise_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateOnPremiseErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
