from typing import Literal

ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_kubernetes_controlplanes_create_workspace_id_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
