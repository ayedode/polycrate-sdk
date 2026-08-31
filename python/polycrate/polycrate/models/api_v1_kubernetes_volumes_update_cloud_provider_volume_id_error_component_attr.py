from typing import Literal

ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponentAttr = Literal["cloud_provider_volume_id"]

API_V1_KUBERNETES_VOLUMES_UPDATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponentAttr
] = {
    "cloud_provider_volume_id",
}


def check_api_v1_kubernetes_volumes_update_cloud_provider_volume_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
