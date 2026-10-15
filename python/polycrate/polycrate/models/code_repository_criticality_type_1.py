from typing import Literal

CodeRepositoryCriticalityType1 = Literal["", "high", "low", "medium"]

CODE_REPOSITORY_CRITICALITY_TYPE_1_VALUES: set[CodeRepositoryCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_code_repository_criticality_type_1(value: str) -> CodeRepositoryCriticalityType1:
    if value in CODE_REPOSITORY_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_CRITICALITY_TYPE_1_VALUES!r}")
