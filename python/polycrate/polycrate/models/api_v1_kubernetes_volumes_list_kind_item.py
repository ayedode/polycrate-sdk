from typing import Literal

ApiV1KubernetesVolumesListKindItem = Literal["generic"]

API_V1_KUBERNETES_VOLUMES_LIST_KIND_ITEM_VALUES: set[ApiV1KubernetesVolumesListKindItem] = {
    "generic",
}


def check_api_v1_kubernetes_volumes_list_kind_item(value: str) -> ApiV1KubernetesVolumesListKindItem:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_KIND_ITEM_VALUES!r}")
