from typing import Literal

ApiV1KubernetesVolumesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_KUBERNETES_VOLUMES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_kubernetes_volumes_list_state_not_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListStateNotErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
