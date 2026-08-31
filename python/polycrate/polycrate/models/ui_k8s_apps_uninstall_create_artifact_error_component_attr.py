from typing import Literal

UiK8SAppsUninstallCreateArtifactErrorComponentAttr = Literal["artifact"]

UI_K8S_APPS_UNINSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateArtifactErrorComponentAttr
] = {
    "artifact",
}


def check_ui_k8s_apps_uninstall_create_artifact_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateArtifactErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
