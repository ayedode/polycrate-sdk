from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_kubernetes_addon_config_revisions_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
