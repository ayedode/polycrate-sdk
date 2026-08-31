from typing import Literal

ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponentAttr = Literal["excluded_from_downtime_until"]

API_V1_KUBERNETES_APPS_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponentAttr
] = {
    "excluded_from_downtime_until",
}


def check_api_v1_kubernetes_apps_create_excluded_from_downtime_until_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
