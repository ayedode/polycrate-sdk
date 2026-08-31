from typing import Literal

ApiV1KubernetesVolumesListNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_VOLUMES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_volumes_list_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
