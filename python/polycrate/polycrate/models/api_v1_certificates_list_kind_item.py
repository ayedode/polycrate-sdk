from typing import Literal

ApiV1CertificatesListKindItem = Literal["mtls", "tls"]

API_V1_CERTIFICATES_LIST_KIND_ITEM_VALUES: set[ApiV1CertificatesListKindItem] = {
    "mtls",
    "tls",
}


def check_api_v1_certificates_list_kind_item(value: str) -> ApiV1CertificatesListKindItem:
    if value in API_V1_CERTIFICATES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_KIND_ITEM_VALUES!r}")
