from typing import Literal

ApiV1KubernetesAddonsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_KUBERNETES_ADDONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_kubernetes_addons_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
