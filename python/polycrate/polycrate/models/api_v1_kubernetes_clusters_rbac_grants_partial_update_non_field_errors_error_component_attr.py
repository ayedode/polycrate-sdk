from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
