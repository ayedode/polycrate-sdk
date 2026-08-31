from typing import Literal

ApiV1ProvidersUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROVIDERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_providers_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
