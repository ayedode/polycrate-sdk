from typing import Literal

ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_apps_discover_create_excluded_from_downtime_until_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
