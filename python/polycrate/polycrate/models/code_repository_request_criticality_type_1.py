from typing import Literal

CodeRepositoryRequestCriticalityType1 = Literal["", "high", "low", "medium"]

CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES: set[CodeRepositoryRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_code_repository_request_criticality_type_1(value: str) -> CodeRepositoryRequestCriticalityType1:
    if value in CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
