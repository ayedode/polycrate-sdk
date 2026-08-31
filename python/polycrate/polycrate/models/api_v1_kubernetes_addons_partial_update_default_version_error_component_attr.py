from typing import Literal

ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponentAttr = Literal["default_version"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_DEFAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponentAttr
] = {
    "default_version",
}


def check_api_v1_kubernetes_addons_partial_update_default_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_DEFAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_DEFAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
