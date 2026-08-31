from typing import Literal

ApiV1KubernetesVolumesListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_KUBERNETES_VOLUMES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_kubernetes_volumes_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListCreatedByComponentErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
