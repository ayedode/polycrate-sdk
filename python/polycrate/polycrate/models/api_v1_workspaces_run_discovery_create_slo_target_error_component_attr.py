from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_workspaces_run_discovery_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateSloTargetErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
