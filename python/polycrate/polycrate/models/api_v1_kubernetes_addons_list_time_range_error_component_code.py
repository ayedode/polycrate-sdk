from typing import Literal

ApiV1KubernetesAddonsListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_ADDONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_addons_list_time_range_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListTimeRangeErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
