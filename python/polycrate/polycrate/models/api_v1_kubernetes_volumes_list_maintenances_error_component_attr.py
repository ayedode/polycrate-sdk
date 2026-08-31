from typing import Literal

ApiV1KubernetesVolumesListMaintenancesErrorComponentAttr = Literal["maintenances"]

API_V1_KUBERNETES_VOLUMES_LIST_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListMaintenancesErrorComponentAttr
] = {
    "maintenances",
}


def check_api_v1_kubernetes_volumes_list_maintenances_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListMaintenancesErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
