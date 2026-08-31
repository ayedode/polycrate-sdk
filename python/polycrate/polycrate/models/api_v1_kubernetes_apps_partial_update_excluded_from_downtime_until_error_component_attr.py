from typing import Literal

ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponentAttr = Literal["excluded_from_downtime_until"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponentAttr
] = {
    "excluded_from_downtime_until",
}


def check_api_v1_kubernetes_apps_partial_update_excluded_from_downtime_until_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateExcludedFromDowntimeUntilErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
