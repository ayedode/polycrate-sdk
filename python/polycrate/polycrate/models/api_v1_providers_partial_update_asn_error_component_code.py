from typing import Literal

ApiV1ProvidersPartialUpdateAsnErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_PARTIAL_UPDATE_ASN_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersPartialUpdateAsnErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_partial_update_asn_error_component_code(
    value: str,
) -> ApiV1ProvidersPartialUpdateAsnErrorComponentCode:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_ASN_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_ASN_ERROR_COMPONENT_CODE_VALUES!r}"
    )
