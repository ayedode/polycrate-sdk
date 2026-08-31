from typing import Literal

ApiV1PopsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_POPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateTolerationsErrorComponentAttr] = {
    "tolerations",
}


def check_api_v1_pops_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PopsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
