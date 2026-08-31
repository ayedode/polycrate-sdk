from typing import Literal

ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_kubernetes_apps_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
