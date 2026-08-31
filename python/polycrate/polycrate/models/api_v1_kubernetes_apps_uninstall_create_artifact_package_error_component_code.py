from typing import Literal

ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_uninstall_create_artifact_package_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateArtifactPackageErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
