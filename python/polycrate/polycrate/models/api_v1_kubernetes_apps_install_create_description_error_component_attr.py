from typing import Literal

ApiV1KubernetesAppsInstallCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_kubernetes_apps_install_create_description_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateDescriptionErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
