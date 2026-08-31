from typing import Literal

ApiV1ProvidersCreateAsnErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_CREATE_ASN_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreateAsnErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_create_asn_error_component_code(value: str) -> ApiV1ProvidersCreateAsnErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_ASN_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_ASN_ERROR_COMPONENT_CODE_VALUES!r}"
    )
