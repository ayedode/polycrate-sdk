from typing import Literal

ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_kubernetes_apps_partial_update_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
