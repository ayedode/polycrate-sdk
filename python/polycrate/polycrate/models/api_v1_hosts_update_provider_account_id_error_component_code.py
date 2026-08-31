from typing import Literal

ApiV1HostsUpdateProviderAccountIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_HOSTS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsUpdateProviderAccountIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_hosts_update_provider_account_id_error_component_code(
    value: str,
) -> ApiV1HostsUpdateProviderAccountIdErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
