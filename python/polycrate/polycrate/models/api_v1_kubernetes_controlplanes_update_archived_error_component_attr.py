from typing import Literal

ApiV1KubernetesControlplanesUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_controlplanes_update_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
