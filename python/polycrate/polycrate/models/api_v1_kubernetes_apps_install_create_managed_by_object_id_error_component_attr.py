from typing import Literal

ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_kubernetes_apps_install_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
