from typing import Literal

ApiV1KubernetesVolumesListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_KUBERNETES_VOLUMES_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_kubernetes_volumes_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListNameExactErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
