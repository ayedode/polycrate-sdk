from typing import Literal

ApiV1PrefixesCreateCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PREFIXES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesCreateCredentialIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_prefixes_create_credential_id_error_component_code(
    value: str,
) -> ApiV1PrefixesCreateCredentialIdErrorComponentCode:
    if value in API_V1_PREFIXES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
