from typing import Literal

ApiV1ProvidersArchiveCreateAsnErrorComponentAttr = Literal["asn"]

API_V1_PROVIDERS_ARCHIVE_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateAsnErrorComponentAttr
] = {
    "asn",
}


def check_api_v1_providers_archive_create_asn_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateAsnErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
