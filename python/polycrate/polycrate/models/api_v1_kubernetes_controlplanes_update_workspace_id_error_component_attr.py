from typing import Literal

ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_kubernetes_controlplanes_update_workspace_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
