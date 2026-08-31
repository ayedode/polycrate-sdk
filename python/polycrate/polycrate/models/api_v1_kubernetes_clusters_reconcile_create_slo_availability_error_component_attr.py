from typing import Literal

ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_kubernetes_clusters_reconcile_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
