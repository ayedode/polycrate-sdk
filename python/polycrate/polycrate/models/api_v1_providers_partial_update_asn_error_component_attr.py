from typing import Literal

ApiV1ProvidersPartialUpdateAsnErrorComponentAttr = Literal["asn"]

API_V1_PROVIDERS_PARTIAL_UPDATE_ASN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateAsnErrorComponentAttr
] = {
    "asn",
}


def check_api_v1_providers_partial_update_asn_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateAsnErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_ASN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_ASN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
