from typing import Literal

ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponentAttr = Literal["provider_object_id"]

API_V1_KUBERNETES_VOLUMES_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponentAttr
] = {
    "provider_object_id",
}


def check_api_v1_kubernetes_volumes_create_provider_object_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
