from typing import Literal

ApiV1KubernetesAppsListKindItem = Literal["external", "helm", "polycrate"]

API_V1_KUBERNETES_APPS_LIST_KIND_ITEM_VALUES: set[ApiV1KubernetesAppsListKindItem] = {
    "external",
    "helm",
    "polycrate",
}


def check_api_v1_kubernetes_apps_list_kind_item(value: str) -> ApiV1KubernetesAppsListKindItem:
    if value in API_V1_KUBERNETES_APPS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_KIND_ITEM_VALUES!r}")
