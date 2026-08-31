from typing import Literal

ApiV1KubernetesControlplanesListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_controlplanes_list_created_at_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesListCreatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
