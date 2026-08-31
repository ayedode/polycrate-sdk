from typing import Literal

ApiV1HostsListScope = Literal["system", "user"]

API_V1_HOSTS_LIST_SCOPE_VALUES: set[ApiV1HostsListScope] = {
    "system",
    "user",
}


def check_api_v1_hosts_list_scope(value: str) -> ApiV1HostsListScope:
    if value in API_V1_HOSTS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_SCOPE_VALUES!r}")
