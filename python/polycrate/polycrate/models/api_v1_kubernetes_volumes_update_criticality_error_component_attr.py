from typing import Literal

ApiV1KubernetesVolumesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_VOLUMES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_volumes_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
