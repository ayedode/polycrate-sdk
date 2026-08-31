from typing import Literal

ApiV1HostsUpdateProviderTypeErrorComponentAttr = Literal["provider_type"]

API_V1_HOSTS_UPDATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateProviderTypeErrorComponentAttr] = {
    "provider_type",
}


def check_api_v1_hosts_update_provider_type_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateProviderTypeErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
