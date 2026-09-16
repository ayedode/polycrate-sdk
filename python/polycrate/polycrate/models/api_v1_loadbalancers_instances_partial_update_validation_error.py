from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_instances_partial_update_annotations_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_partial_update_config_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_partial_update_haproxy_defaults_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_partial_update_labels_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_partial_update_non_field_errors_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_partial_update_ports_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_partial_update_resource_limits_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_partial_update_wizard_ports_error_component import (
        ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersInstancesPartialUpdateValidationError")


@_attrs_define
class ApiV1LoadbalancersInstancesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent |
            ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent |
            ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponent |
            ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent |
            ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent |
            ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent |
            ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent
        | ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent
        | ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponent
        | ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent
        | ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent
        | ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent
        | ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_instances_partial_update_annotations_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_config_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_labels_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_non_field_errors_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_ports_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_resource_limits_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_wizard_ports_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent):
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
        from ..models.api_v1_loadbalancers_instances_partial_update_annotations_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_config_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_haproxy_defaults_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_labels_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_non_field_errors_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_ports_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_resource_limits_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_partial_update_wizard_ports_error_component import (
            ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent
                | ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent
                | ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponent
                | ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent
                | ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent
                | ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent
                | ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_0 = (
                        ApiV1LoadbalancersInstancesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_1 = (
                        ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_2 = (
                        ApiV1LoadbalancersInstancesPartialUpdatePortsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_3 = (
                        ApiV1LoadbalancersInstancesPartialUpdateWizardPortsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_4 = (
                        ApiV1LoadbalancersInstancesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_5 = (
                        ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_6 = (
                        ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_7 = (
                    ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_instances_partial_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_instances_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_instances_partial_update_validation_error.additional_properties = d
        return api_v1_loadbalancers_instances_partial_update_validation_error

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
