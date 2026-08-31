from typing import Literal

ApiV1ProvidersPartialUpdateCertificationsErrorComponentAttr = Literal["certifications"]

API_V1_PROVIDERS_PARTIAL_UPDATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateCertificationsErrorComponentAttr
] = {
    "certifications",
}


def check_api_v1_providers_partial_update_certifications_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateCertificationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
