from typing import Literal

ApiV1HostsListWorkerPoolErrorComponentAttr = Literal["worker_pool"]

API_V1_HOSTS_LIST_WORKER_POOL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListWorkerPoolErrorComponentAttr] = {
    "worker_pool",
}


def check_api_v1_hosts_list_worker_pool_error_component_attr(value: str) -> ApiV1HostsListWorkerPoolErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_WORKER_POOL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_WORKER_POOL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
