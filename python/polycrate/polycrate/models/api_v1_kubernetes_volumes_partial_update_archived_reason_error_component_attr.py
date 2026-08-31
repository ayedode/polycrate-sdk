from typing import Literal

ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_kubernetes_volumes_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
