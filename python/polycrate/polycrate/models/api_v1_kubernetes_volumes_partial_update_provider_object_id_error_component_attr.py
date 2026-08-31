from typing import Literal

ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponentAttr = Literal["provider_object_id"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponentAttr
] = {
    "provider_object_id",
}


def check_api_v1_kubernetes_volumes_partial_update_provider_object_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
