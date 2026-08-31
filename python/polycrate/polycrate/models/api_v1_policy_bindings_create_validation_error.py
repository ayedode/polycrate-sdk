from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_policy_bindings_create_applied_error_component import (
        ApiV1PolicyBindingsCreateAppliedErrorComponent,
    )
    from ..models.api_v1_policy_bindings_create_enabled_error_component import (
        ApiV1PolicyBindingsCreateEnabledErrorComponent,
    )
    from ..models.api_v1_policy_bindings_create_execution_log_error_component import (
        ApiV1PolicyBindingsCreateExecutionLogErrorComponent,
    )
    from ..models.api_v1_policy_bindings_create_non_field_errors_error_component import (
        ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_policy_bindings_create_policy_id_error_component import (
        ApiV1PolicyBindingsCreatePolicyIdErrorComponent,
    )
    from ..models.api_v1_policy_bindings_create_scope_error_component import (
        ApiV1PolicyBindingsCreateScopeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PolicyBindingsCreateValidationError")


@_attrs_define
class ApiV1PolicyBindingsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PolicyBindingsCreateAppliedErrorComponent | ApiV1PolicyBindingsCreateEnabledErrorComponent |
            ApiV1PolicyBindingsCreateExecutionLogErrorComponent | ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent |
            ApiV1PolicyBindingsCreatePolicyIdErrorComponent | ApiV1PolicyBindingsCreateScopeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PolicyBindingsCreateAppliedErrorComponent
        | ApiV1PolicyBindingsCreateEnabledErrorComponent
        | ApiV1PolicyBindingsCreateExecutionLogErrorComponent
        | ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent
        | ApiV1PolicyBindingsCreatePolicyIdErrorComponent
        | ApiV1PolicyBindingsCreateScopeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_policy_bindings_create_applied_error_component import (
            ApiV1PolicyBindingsCreateAppliedErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_enabled_error_component import (
            ApiV1PolicyBindingsCreateEnabledErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_non_field_errors_error_component import (
            ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_policy_id_error_component import (
            ApiV1PolicyBindingsCreatePolicyIdErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_scope_error_component import (
            ApiV1PolicyBindingsCreateScopeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsCreatePolicyIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsCreateEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsCreateAppliedErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_policy_bindings_create_applied_error_component import (
            ApiV1PolicyBindingsCreateAppliedErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_enabled_error_component import (
            ApiV1PolicyBindingsCreateEnabledErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_execution_log_error_component import (
            ApiV1PolicyBindingsCreateExecutionLogErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_non_field_errors_error_component import (
            ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_policy_id_error_component import (
            ApiV1PolicyBindingsCreatePolicyIdErrorComponent,
        )
        from ..models.api_v1_policy_bindings_create_scope_error_component import (
            ApiV1PolicyBindingsCreateScopeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PolicyBindingsCreateAppliedErrorComponent
                | ApiV1PolicyBindingsCreateEnabledErrorComponent
                | ApiV1PolicyBindingsCreateExecutionLogErrorComponent
                | ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent
                | ApiV1PolicyBindingsCreatePolicyIdErrorComponent
                | ApiV1PolicyBindingsCreateScopeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_create_error_type_0 = (
                        ApiV1PolicyBindingsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_create_error_type_1 = (
                        ApiV1PolicyBindingsCreatePolicyIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_create_error_type_2 = (
                        ApiV1PolicyBindingsCreateEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_create_error_type_3 = (
                        ApiV1PolicyBindingsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_create_error_type_4 = (
                        ApiV1PolicyBindingsCreateAppliedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_policy_bindings_create_error_type_5 = (
                    ApiV1PolicyBindingsCreateExecutionLogErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_policy_bindings_create_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_policy_bindings_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_policy_bindings_create_validation_error.additional_properties = d
        return api_v1_policy_bindings_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
