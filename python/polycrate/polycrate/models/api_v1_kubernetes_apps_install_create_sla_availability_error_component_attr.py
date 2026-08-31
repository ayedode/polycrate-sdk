from typing import Literal

ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_kubernetes_apps_install_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
