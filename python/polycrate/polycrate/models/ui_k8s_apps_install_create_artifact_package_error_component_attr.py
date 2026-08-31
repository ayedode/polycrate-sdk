from typing import Literal

UiK8SAppsInstallCreateArtifactPackageErrorComponentAttr = Literal["artifact_package"]

UI_K8S_APPS_INSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_ui_k8s_apps_install_create_artifact_package_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateArtifactPackageErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
