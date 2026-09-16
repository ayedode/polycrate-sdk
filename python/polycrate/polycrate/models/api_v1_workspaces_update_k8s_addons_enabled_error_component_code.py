from typing import Literal

ApiV1WorkspacesUpdateK8SAddonsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_K8S_ADDONS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateK8SAddonsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_k8s_addons_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateK8SAddonsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_K8S_ADDONS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_K8S_ADDONS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
