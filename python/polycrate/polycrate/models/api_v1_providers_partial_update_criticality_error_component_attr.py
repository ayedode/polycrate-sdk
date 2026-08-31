from typing import Literal

ApiV1ProvidersPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_providers_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
