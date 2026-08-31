from typing import Literal

ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponentAttr = Literal["provider_object_name"]

API_V1_KUBERNETES_VOLUMES_UPDATE_PROVIDER_OBJECT_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponentAttr
] = {
    "provider_object_name",
}


def check_api_v1_kubernetes_volumes_update_provider_object_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_PROVIDER_OBJECT_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_PROVIDER_OBJECT_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
