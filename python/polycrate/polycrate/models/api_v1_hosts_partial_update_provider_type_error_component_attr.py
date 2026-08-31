from typing import Literal

ApiV1HostsPartialUpdateProviderTypeErrorComponentAttr = Literal["provider_type"]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateProviderTypeErrorComponentAttr
] = {
    "provider_type",
}


def check_api_v1_hosts_partial_update_provider_type_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateProviderTypeErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
