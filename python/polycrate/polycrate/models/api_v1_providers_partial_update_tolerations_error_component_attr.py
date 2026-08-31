from typing import Literal

ApiV1ProvidersPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROVIDERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_providers_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
