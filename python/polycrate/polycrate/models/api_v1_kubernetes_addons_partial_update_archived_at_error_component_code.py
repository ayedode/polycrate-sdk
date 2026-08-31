from typing import Literal

ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_addons_partial_update_archived_at_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
