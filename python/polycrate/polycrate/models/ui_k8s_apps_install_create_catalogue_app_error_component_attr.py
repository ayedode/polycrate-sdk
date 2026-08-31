from typing import Literal

UiK8SAppsInstallCreateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

UI_K8S_APPS_INSTALL_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_ui_k8s_apps_install_create_catalogue_app_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateCatalogueAppErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
