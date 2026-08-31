from typing import Literal

ApiV1HostsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_HOSTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_hosts_update_criticality_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
