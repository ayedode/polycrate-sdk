from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_kubernetes_addon_config_revisions_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
