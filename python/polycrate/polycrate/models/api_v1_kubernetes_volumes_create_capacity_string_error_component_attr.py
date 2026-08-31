from typing import Literal

ApiV1KubernetesVolumesCreateCapacityStringErrorComponentAttr = Literal["capacity_string"]

API_V1_KUBERNETES_VOLUMES_CREATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateCapacityStringErrorComponentAttr
] = {
    "capacity_string",
}


def check_api_v1_kubernetes_volumes_create_capacity_string_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateCapacityStringErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
