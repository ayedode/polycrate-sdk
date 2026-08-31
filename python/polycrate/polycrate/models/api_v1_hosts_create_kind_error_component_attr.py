from typing import Literal

ApiV1HostsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_HOSTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_hosts_create_kind_error_component_attr(value: str) -> ApiV1HostsCreateKindErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
