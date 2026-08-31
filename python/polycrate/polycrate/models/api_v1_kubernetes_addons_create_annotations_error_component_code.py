from typing import Literal

ApiV1KubernetesAddonsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_ADDONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_addons_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
