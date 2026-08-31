from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_kubernetes_addon_config_revisions_list_time_range_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
