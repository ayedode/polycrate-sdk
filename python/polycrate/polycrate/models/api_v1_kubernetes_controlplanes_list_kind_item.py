from typing import Literal

ApiV1KubernetesControlplanesListKindItem = Literal["generic"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_KIND_ITEM_VALUES: set[ApiV1KubernetesControlplanesListKindItem] = {
    "generic",
}


def check_api_v1_kubernetes_controlplanes_list_kind_item(value: str) -> ApiV1KubernetesControlplanesListKindItem:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_KIND_ITEM_VALUES!r}"
    )
