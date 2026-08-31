from typing import Literal

ApiV1ProvidersUpdateCertificationsErrorComponentAttr = Literal["certifications"]

API_V1_PROVIDERS_UPDATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersUpdateCertificationsErrorComponentAttr
] = {
    "certifications",
}


def check_api_v1_providers_update_certifications_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateCertificationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
