from typing import Literal

ApiV1IpaddressesUpdateCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_IPADDRESSES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesUpdateCredentialIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_ipaddresses_update_credential_id_error_component_code(
    value: str,
) -> ApiV1IpaddressesUpdateCredentialIdErrorComponentCode:
    if value in API_V1_IPADDRESSES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
