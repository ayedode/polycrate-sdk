from typing import Literal

ProductDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[ProductDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_product_detail_request_criticality_type_1(value: str) -> ProductDetailRequestCriticalityType1:
    if value in PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
