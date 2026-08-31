from typing import Literal

ApiV1HostsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_HOSTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_hosts_create_criticality_error_component_attr(
    value: str,
) -> ApiV1HostsCreateCriticalityErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
