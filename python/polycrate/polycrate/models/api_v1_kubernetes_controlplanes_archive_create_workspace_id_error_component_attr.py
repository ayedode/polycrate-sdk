from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_kubernetes_controlplanes_archive_create_workspace_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateWorkspaceIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
