from typing import Literal

ApiV1HostsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_HOSTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_hosts_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
