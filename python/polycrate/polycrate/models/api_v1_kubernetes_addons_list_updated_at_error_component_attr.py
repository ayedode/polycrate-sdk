from typing import Literal

ApiV1KubernetesAddonsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_KUBERNETES_ADDONS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_kubernetes_addons_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsListUpdatedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
