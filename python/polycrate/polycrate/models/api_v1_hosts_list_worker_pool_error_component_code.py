from typing import Literal

ApiV1HostsListWorkerPoolErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_HOSTS_LIST_WORKER_POOL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListWorkerPoolErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_hosts_list_worker_pool_error_component_code(value: str) -> ApiV1HostsListWorkerPoolErrorComponentCode:
    if value in API_V1_HOSTS_LIST_WORKER_POOL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_WORKER_POOL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
