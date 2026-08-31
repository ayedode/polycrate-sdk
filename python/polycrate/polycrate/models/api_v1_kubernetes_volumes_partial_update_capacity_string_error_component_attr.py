from typing import Literal

ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponentAttr = Literal["capacity_string"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponentAttr
] = {
    "capacity_string",
}


def check_api_v1_kubernetes_volumes_partial_update_capacity_string_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
