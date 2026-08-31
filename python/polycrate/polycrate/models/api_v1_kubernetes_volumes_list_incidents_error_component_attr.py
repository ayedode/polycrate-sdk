from typing import Literal

ApiV1KubernetesVolumesListIncidentsErrorComponentAttr = Literal["incidents"]

API_V1_KUBERNETES_VOLUMES_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListIncidentsErrorComponentAttr
] = {
    "incidents",
}


def check_api_v1_kubernetes_volumes_list_incidents_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListIncidentsErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
