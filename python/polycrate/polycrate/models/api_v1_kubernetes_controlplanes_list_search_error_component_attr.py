from typing import Literal

ApiV1KubernetesControlplanesListSearchErrorComponentAttr = Literal["search"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_kubernetes_controlplanes_list_search_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListSearchErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
