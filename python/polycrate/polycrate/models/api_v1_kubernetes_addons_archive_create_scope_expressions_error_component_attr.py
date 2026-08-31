from typing import Literal

ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponentAttr = Literal["scope_expressions"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponentAttr
] = {
    "scope_expressions",
}


def check_api_v1_kubernetes_addons_archive_create_scope_expressions_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
