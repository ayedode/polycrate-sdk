from typing import Literal

ApiV1KubernetesControlplanesListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_list_search_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesListSearchErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
