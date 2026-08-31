from typing import Literal

ApiV1KubernetesAppsInstallCreateArtifactErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreateArtifactErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_install_create_artifact_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateArtifactErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
