from typing import Literal

ApiV1KubernetesAddonsListKindItem = Literal["generic"]

API_V1_KUBERNETES_ADDONS_LIST_KIND_ITEM_VALUES: set[ApiV1KubernetesAddonsListKindItem] = {
    "generic",
}


def check_api_v1_kubernetes_addons_list_kind_item(value: str) -> ApiV1KubernetesAddonsListKindItem:
    if value in API_V1_KUBERNETES_ADDONS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_KIND_ITEM_VALUES!r}")
