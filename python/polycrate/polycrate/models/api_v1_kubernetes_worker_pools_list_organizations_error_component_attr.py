from typing import Literal

ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_kubernetes_worker_pools_list_organizations_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
