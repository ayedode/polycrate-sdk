from typing import Literal

ApiV1HostsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_HOSTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_hosts_update_kind_error_component_attr(value: str) -> ApiV1HostsUpdateKindErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
