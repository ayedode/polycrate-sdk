from typing import Literal

UiK8SAppsUninstallCreateArtifactPackageErrorComponentAttr = Literal["artifact_package"]

UI_K8S_APPS_UNINSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_ui_k8s_apps_uninstall_create_artifact_package_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateArtifactPackageErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
