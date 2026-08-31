from typing import Literal

ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponentAttr = Literal["provider_object_name"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PROVIDER_OBJECT_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponentAttr
] = {
    "provider_object_name",
}


def check_api_v1_kubernetes_volumes_partial_update_provider_object_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PROVIDER_OBJECT_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PROVIDER_OBJECT_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
