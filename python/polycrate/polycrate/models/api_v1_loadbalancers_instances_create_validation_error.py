from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_instances_create_annotations_error_component import (
        ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_config_error_component import (
        ApiV1LoadbalancersInstancesCreateConfigErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_consumer_meta_error_component import (
        ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_display_name_error_component import (
        ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_haproxy_defaults_error_component import (
        ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_labels_error_component import (
        ApiV1LoadbalancersInstancesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_non_field_errors_error_component import (
        ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_organization_error_component import (
        ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_ports_error_component import (
        ApiV1LoadbalancersInstancesCreatePortsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_resource_limits_error_component import (
        ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_wizard_ports_error_component import (
        ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_create_workspace_error_component import (
        ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersInstancesCreateValidationError")


@_attrs_define
class ApiV1LoadbalancersInstancesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent |
            ApiV1LoadbalancersInstancesCreateConfigErrorComponent |
            ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent |
            ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent |
            ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponent |
            ApiV1LoadbalancersInstancesCreateLabelsErrorComponent |
            ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent |
            ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent |
            ApiV1LoadbalancersInstancesCreatePortsErrorComponent |
            ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent |
            ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent |
            ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent
        | ApiV1LoadbalancersInstancesCreateConfigErrorComponent
        | ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent
        | ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent
        | ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponent
        | ApiV1LoadbalancersInstancesCreateLabelsErrorComponent
        | ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent
        | ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent
        | ApiV1LoadbalancersInstancesCreatePortsErrorComponent
        | ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent
        | ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent
        | ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_instances_create_annotations_error_component import (
            ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_config_error_component import (
            ApiV1LoadbalancersInstancesCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_consumer_meta_error_component import (
            ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_display_name_error_component import (
            ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_labels_error_component import (
            ApiV1LoadbalancersInstancesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_non_field_errors_error_component import (
            ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_organization_error_component import (
            ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_ports_error_component import (
            ApiV1LoadbalancersInstancesCreatePortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_resource_limits_error_component import (
            ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_wizard_ports_error_component import (
            ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_workspace_error_component import (
            ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreatePortsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent):
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
        from ..models.api_v1_loadbalancers_instances_create_annotations_error_component import (
            ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_config_error_component import (
            ApiV1LoadbalancersInstancesCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_consumer_meta_error_component import (
            ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_display_name_error_component import (
            ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_haproxy_defaults_error_component import (
            ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_labels_error_component import (
            ApiV1LoadbalancersInstancesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_non_field_errors_error_component import (
            ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_organization_error_component import (
            ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_ports_error_component import (
            ApiV1LoadbalancersInstancesCreatePortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_resource_limits_error_component import (
            ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_wizard_ports_error_component import (
            ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_create_workspace_error_component import (
            ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent
                | ApiV1LoadbalancersInstancesCreateConfigErrorComponent
                | ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent
                | ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent
                | ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponent
                | ApiV1LoadbalancersInstancesCreateLabelsErrorComponent
                | ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent
                | ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent
                | ApiV1LoadbalancersInstancesCreatePortsErrorComponent
                | ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent
                | ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent
                | ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_0 = (
                        ApiV1LoadbalancersInstancesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_1 = (
                        ApiV1LoadbalancersInstancesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_2 = (
                        ApiV1LoadbalancersInstancesCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_3 = (
                        ApiV1LoadbalancersInstancesCreatePortsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_4 = (
                        ApiV1LoadbalancersInstancesCreateWizardPortsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_5 = (
                        ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_6 = (
                        ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_7 = (
                        ApiV1LoadbalancersInstancesCreateOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_8 = (
                        ApiV1LoadbalancersInstancesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_9 = (
                        ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_create_error_type_10 = (
                        ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_instances_create_error_type_11 = (
                    ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_instances_create_error_type_11

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_instances_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_instances_create_validation_error.additional_properties = d
        return api_v1_loadbalancers_instances_create_validation_error

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
