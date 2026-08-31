from typing import Literal

ApiV1KubernetesAddonsArchiveCreateOrderErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_ORDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateOrderErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_kubernetes_addons_archive_create_order_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateOrderErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_ORDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_ORDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
