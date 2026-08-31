from typing import Literal

ApiV1HostsPartialUpdateProviderAccountIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsPartialUpdateProviderAccountIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_hosts_partial_update_provider_account_id_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdateProviderAccountIdErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
