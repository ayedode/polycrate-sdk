from typing import Literal

ApiV1KubernetesVolumesUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_KUBERNETES_VOLUMES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_kubernetes_volumes_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateProviderIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
