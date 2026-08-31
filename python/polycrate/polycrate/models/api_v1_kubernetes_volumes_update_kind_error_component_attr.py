from typing import Literal

ApiV1KubernetesVolumesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_VOLUMES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_volumes_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
