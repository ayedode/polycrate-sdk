from typing import Literal

ApiV1KubernetesVolumesListStateErrorComponentAttr = Literal["state"]

API_V1_KUBERNETES_VOLUMES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_kubernetes_volumes_list_state_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListStateErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
