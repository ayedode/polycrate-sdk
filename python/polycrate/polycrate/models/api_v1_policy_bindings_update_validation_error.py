from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_policy_bindings_update_applied_error_component import (
        ApiV1PolicyBindingsUpdateAppliedErrorComponent,
    )
    from ..models.api_v1_policy_bindings_update_enabled_error_component import (
        ApiV1PolicyBindingsUpdateEnabledErrorComponent,
    )
    from ..models.api_v1_policy_bindings_update_execution_log_error_component import (
        ApiV1PolicyBindingsUpdateExecutionLogErrorComponent,
    )
    from ..models.api_v1_policy_bindings_update_non_field_errors_error_component import (
        ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_policy_bindings_update_policy_id_error_component import (
        ApiV1PolicyBindingsUpdatePolicyIdErrorComponent,
    )
    from ..models.api_v1_policy_bindings_update_scope_error_component import (
        ApiV1PolicyBindingsUpdateScopeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PolicyBindingsUpdateValidationError")


@_attrs_define
class ApiV1PolicyBindingsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PolicyBindingsUpdateAppliedErrorComponent | ApiV1PolicyBindingsUpdateEnabledErrorComponent |
            ApiV1PolicyBindingsUpdateExecutionLogErrorComponent | ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent |
            ApiV1PolicyBindingsUpdatePolicyIdErrorComponent | ApiV1PolicyBindingsUpdateScopeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PolicyBindingsUpdateAppliedErrorComponent
        | ApiV1PolicyBindingsUpdateEnabledErrorComponent
        | ApiV1PolicyBindingsUpdateExecutionLogErrorComponent
        | ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent
        | ApiV1PolicyBindingsUpdatePolicyIdErrorComponent
        | ApiV1PolicyBindingsUpdateScopeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_policy_bindings_update_applied_error_component import (
            ApiV1PolicyBindingsUpdateAppliedErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_enabled_error_component import (
            ApiV1PolicyBindingsUpdateEnabledErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_non_field_errors_error_component import (
            ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_policy_id_error_component import (
            ApiV1PolicyBindingsUpdatePolicyIdErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_scope_error_component import (
            ApiV1PolicyBindingsUpdateScopeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsUpdatePolicyIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsUpdateEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsUpdateAppliedErrorComponent):
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
        from ..models.api_v1_policy_bindings_update_applied_error_component import (
            ApiV1PolicyBindingsUpdateAppliedErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_enabled_error_component import (
            ApiV1PolicyBindingsUpdateEnabledErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_execution_log_error_component import (
            ApiV1PolicyBindingsUpdateExecutionLogErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_non_field_errors_error_component import (
            ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_policy_id_error_component import (
            ApiV1PolicyBindingsUpdatePolicyIdErrorComponent,
        )
        from ..models.api_v1_policy_bindings_update_scope_error_component import (
            ApiV1PolicyBindingsUpdateScopeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PolicyBindingsUpdateAppliedErrorComponent
                | ApiV1PolicyBindingsUpdateEnabledErrorComponent
                | ApiV1PolicyBindingsUpdateExecutionLogErrorComponent
                | ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent
                | ApiV1PolicyBindingsUpdatePolicyIdErrorComponent
                | ApiV1PolicyBindingsUpdateScopeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_update_error_type_0 = (
                        ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_update_error_type_1 = (
                        ApiV1PolicyBindingsUpdatePolicyIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_update_error_type_2 = (
                        ApiV1PolicyBindingsUpdateEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_update_error_type_3 = (
                        ApiV1PolicyBindingsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_update_error_type_4 = (
                        ApiV1PolicyBindingsUpdateAppliedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_policy_bindings_update_error_type_5 = (
                    ApiV1PolicyBindingsUpdateExecutionLogErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_policy_bindings_update_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_policy_bindings_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_policy_bindings_update_validation_error.additional_properties = d
        return api_v1_policy_bindings_update_validation_error

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
