from typing import Literal

ApiV1KubernetesAddonsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_ADDONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_addons_update_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
