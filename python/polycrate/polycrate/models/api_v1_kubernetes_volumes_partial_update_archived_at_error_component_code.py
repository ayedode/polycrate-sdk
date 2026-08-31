from typing import Literal

ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_volumes_partial_update_archived_at_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
