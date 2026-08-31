from typing import Literal

ApiV1ProvidersUpdateAsnErrorComponentAttr = Literal["asn"]

API_V1_PROVIDERS_UPDATE_ASN_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateAsnErrorComponentAttr] = {
    "asn",
}


def check_api_v1_providers_update_asn_error_component_attr(value: str) -> ApiV1ProvidersUpdateAsnErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_ASN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ASN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
