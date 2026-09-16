from typing import Literal

ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_kubernetes_controlplanes_create_workspace_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
