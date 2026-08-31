from typing import Literal

ApiV1CertificatesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_certificates_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
