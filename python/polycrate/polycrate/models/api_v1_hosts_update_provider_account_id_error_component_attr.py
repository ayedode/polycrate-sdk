from typing import Literal

ApiV1HostsUpdateProviderAccountIdErrorComponentAttr = Literal["provider_account_id"]

API_V1_HOSTS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsUpdateProviderAccountIdErrorComponentAttr
] = {
    "provider_account_id",
}


def check_api_v1_hosts_update_provider_account_id_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateProviderAccountIdErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
