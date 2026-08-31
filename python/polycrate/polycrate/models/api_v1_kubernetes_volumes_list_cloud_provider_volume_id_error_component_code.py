from typing import Literal

ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_KUBERNETES_VOLUMES_LIST_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_list_cloud_provider_volume_id_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
